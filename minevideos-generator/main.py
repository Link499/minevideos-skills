"""
MineVideos AI 视频生成技能
基于火山引擎 Seedance 大模型，支持 T2V / I2V / R2V 三种模式
"""

import os
import sys
import json
import time
import argparse
from coze_workload_identity import requests

# ── 配置 ──────────────────────────────────────────────
SEEDANCE_API_BASE = "https://ark.cn-beijing.volces.com/api/v3"
MODEL_FAST = "doubao-seedance-2-0-fast-260128"
MODEL_STANDARD = "doubao-seedance-2-0-260128"

# 凭证：火山引擎 API Key
# 通过 skill_draft_credential 配置后自动注入
CREDENTIAL_ENV = "COZE_VOLCENGINE_KEY_7656684812945719311"


def get_api_key():
    """获取火山引擎 API Key"""
    key = os.getenv(CREDENTIAL_ENV)
    if not key:
        raise ValueError(
            "未配置火山引擎 API Key。"
            "请通过技能凭证配置页面填写 VOLCENGINE_API_KEY。"
        )
    return key


def build_headers(api_key: str) -> dict:
    """构建请求头"""
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }


def create_video_task(
    api_key: str,
    model: str,
    prompt: str,
    mode: str = "t2v",
    image_url: str = None,
    reference_url: str = None,
) -> dict:
    """
    创建视频生成任务

    Args:
        api_key: 火山引擎 API Key
        model: 模型名称 (fast / standard)
        prompt: 视频描述
        mode: 生成模式 t2v/i2v/r2v
        image_url: 图片URL (I2V模式)
        reference_url: 参考视频URL (R2V模式)

    Returns:
        任务创建结果 dict
    """
    url = f"{SEEDANCE_API_BASE}/content/generation"
    headers = build_headers(api_key)

    model_id = MODEL_FAST if model == "fast" else MODEL_STANDARD

    # 构建请求体
    payload = {
        "model": model_id,
        "content": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                ],
            }
        ],
        "stream": False,
    }

    # 根据模式添加内容
    content_list = payload["content"][0]["content"]

    if mode == "i2v" and image_url:
        content_list.append({
            "type": "image_url",
            "image_url": {"url": image_url},
        })
    elif mode == "r2v" and reference_url:
        content_list.append({
            "type": "video_url",
            "video_url": {"url": reference_url},
        })

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)

        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "task_id": data.get("id", ""),
                "status": data.get("status", "processing"),
                "message": "视频生成任务已提交",
                "estimated_time": "约2-5分钟",
                "raw": data,
            }
        else:
            # fast 模型失败时尝试降级到 standard
            if model == "fast":
                return create_video_task(
                    api_key, "standard", prompt, mode, image_url, reference_url
                )
            return {
                "success": False,
                "error": f"API 请求失败: HTTP {response.status_code}",
                "detail": response.text[:500],
            }

    except requests.exceptions.RequestException as e:
        if model == "fast":
            return create_video_task(
                api_key, "standard", prompt, mode, image_url, reference_url
            )
        return {
            "success": False,
            "error": f"请求异常: {str(e)}",
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"未知错误: {str(e)}",
        }


def query_task(api_key: str, task_id: str) -> dict:
    """
    查询视频生成任务状态

    Args:
        api_key: 火山引擎 API Key
        task_id: 任务ID

    Returns:
        任务状态 dict
    """
    url = f"{SEEDANCE_API_BASE}/content/generation/{task_id}"
    headers = build_headers(api_key)

    try:
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200:
            data = response.json()
            status = data.get("status", "unknown")

            result = {
                "success": True,
                "task_id": task_id,
                "status": status,
            }

            if status == "completed":
                # 提取视频URL
                content = data.get("content", [])
                video_url = ""
                cover_url = ""
                for item in content:
                    if item.get("role") == "assistant":
                        for c in item.get("content", []):
                            if c.get("type") == "video_url":
                                video_url = c.get("video_url", {}).get("url", "")
                            elif c.get("type") == "image_url":
                                cover_url = c.get("image_url", {}).get("url", "")
                result["video_url"] = video_url
                result["cover_url"] = cover_url
            elif status == "failed":
                result["error"] = data.get("error", {}).get("message", "生成失败")

            return result
        else:
            return {
                "success": False,
                "error": f"查询失败: HTTP {response.status_code}",
                "detail": response.text[:500],
            }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"请求异常: {str(e)}",
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"未知错误: {str(e)}",
        }


def wait_for_completion(api_key: str, task_id: str, max_wait: int = 600, interval: int = 15) -> dict:
    """
    等待视频生成完成（轮询）

    Args:
        api_key: 火山引擎 API Key
        task_id: 任务ID
        max_wait: 最大等待时间(秒)
        interval: 轮询间隔(秒)

    Returns:
        最终任务状态 dict
    """
    start_time = time.time()
    while time.time() - start_time < max_wait:
        result = query_task(api_key, task_id)
        if not result.get("success"):
            return result

        status = result.get("status")
        if status == "completed":
            return result
        elif status == "failed":
            return result

        print(f"[等待中] 任务 {task_id} 状态: {status}，{interval}秒后重试...")
        time.sleep(interval)

    return {
        "success": False,
        "task_id": task_id,
        "status": "timeout",
        "error": f"等待超时（{max_wait}秒），请稍后手动查询",
    }


def main():
    parser = argparse.ArgumentParser(description="MineVideos AI 视频生成")
    parser.add_argument("--mode", choices=["t2v", "i2v", "r2v"], default="t2v",
                        help="生成模式: t2v(文生视频) / i2v(图生视频) / r2v(参考视频)")
    parser.add_argument("--prompt", type=str, default="",
                        help="视频描述文本")
    parser.add_argument("--image_url", type=str, default=None,
                        help="输入图片URL (I2V模式)")
    parser.add_argument("--reference_url", type=str, default=None,
                        help="参考视频URL (R2V模式)")
    parser.add_argument("--model", choices=["fast", "standard"], default="fast",
                        help="模型选择: fast(快速) / standard(标准)")
    parser.add_argument("--task_id", type=str, default=None,
                        help="查询已有任务状态")
    parser.add_argument("--query", action="store_true",
                        help="查询任务状态模式")
    parser.add_argument("--wait", action="store_true",
                        help="等待任务完成")
    parser.add_argument("--max_wait", type=int, default=600,
                        help="最大等待时间(秒)")

    args = parser.parse_args()

    try:
        api_key = get_api_key()
    except ValueError as e:
        print(json.dumps({"success": False, "error": str(e)}, ensure_ascii=False))
        sys.exit(1)

    # 查询模式
    if args.query and args.task_id:
        result = query_task(api_key, args.task_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # 等待模式
    if args.wait and args.task_id:
        result = wait_for_completion(api_key, args.task_id, args.max_wait)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # 生成模式 - 校验参数
    if not args.prompt:
        print(json.dumps({
            "success": False,
            "error": "请提供视频描述 (--prompt)",
        }, ensure_ascii=False))
        sys.exit(1)

    if args.mode == "i2v" and not args.image_url:
        print(json.dumps({
            "success": False,
            "error": "I2V模式需要提供图片URL (--image_url)",
        }, ensure_ascii=False))
        sys.exit(1)

    if args.mode == "r2v" and not args.reference_url:
        print(json.dumps({
            "success": False,
            "error": "R2V模式需要提供参考视频URL (--reference_url)",
        }, ensure_ascii=False))
        sys.exit(1)

    # 提交任务
    result = create_video_task(
        api_key=api_key,
        model=args.model,
        prompt=args.prompt,
        mode=args.mode,
        image_url=args.image_url,
        reference_url=args.reference_url,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
