---
name: minevideos-generator
description: AI视频生成技能，支持文本生视频、图片生视频、参考视频生视频三种模式，基于火山引擎Seedance大模型。当用户提到生成视频、AI视频、文生视频、图生视频、视频创作、Seedance、MineVideos、做个视频、帮我生成视频等与AI视频生成相关的需求时使用此技能。
---

# MineVideos AI 视频生成

基于火山引擎 Seedance 大模型的 AI 视频生成技能。支持文本生视频(T2V)、图片生视频(I2V)、参考视频生视频(R2V) 三种模式。

## 何时使用

- 用户要求生成视频、AI视频、文生视频、图生视频
- 用户提到 Seedance、MineVideos、视频创作
- 用户上传图片/文字描述并要求生成视频内容

## 工作流程

### 1. 确定生成模式

根据用户输入判断使用哪种模式：

| 模式 | 触发条件 | 输入要求 |
|------|---------|---------|
| T2V (文生视频) | 用户只提供文字描述 | prompt (必填) |
| I2V (图生视频) | 用户上传图片 + 描述 | image_url (必填), prompt (可选) |
| R2V (参考视频) | 用户要求参考某个视频风格 | reference_url (必填), prompt (可选) |

### 2. 调用生成脚本

```bash
python main.py --mode <t2v|i2v|r2v> --prompt "<描述>" [--image_url "<图片URL>"] [--reference_url "<参考URL>"] [--model fast|standard]
```

**参数说明：**

| 参数 | 必填 | 说明 |
|------|------|------|
| `--mode` | 是 | 生成模式：t2v / i2v / r2v |
| `--prompt` | 是 | 视频描述文本，支持中英文 |
| `--image_url` | I2V模式必填 | 输入图片的URL地址 |
| `--reference_url` | R2V模式必填 | 参考视频的URL地址 |
| `--model` | 否 | 模型选择：fast(快速)/standard(标准)，默认fast |

### 3. 输出格式

脚本返回 JSON 格式结果：

```json
{
  "success": true,
  "task_id": "xxx",
  "status": "processing",
  "message": "视频生成任务已提交",
  "estimated_time": "约2-5分钟"
}
```

任务完成后通过 task_id 查询结果：

```bash
python main.py --query --task_id "<task_id>"
```

返回：

```json
{
  "success": true,
  "task_id": "xxx",
  "status": "completed",
  "video_url": "https://...",
  "cover_url": "https://..."
}
```

## 凭据配置

本技能需要火山引擎 API Key 才能调用 Seedance 模型。凭证通过环境变量自动注入，无需手动配置。

## 边界情况

- **prompt 为空**：提示用户至少提供文字描述或图片
- **API 调用失败**：返回错误信息，建议检查 API Key 或重试
- **模型不可用**：fast 模型失败时自动降级到 standard 模型
- **图片URL无效**：提示用户检查图片链接是否可公开访问

## Prompt 优化建议

生成高质量视频的关键是好的 prompt：
- 描述画面主体、动作、场景、光线、风格
- 加入镜头运动描述（推近、拉远、环绕、跟随）
- 指定画面风格（电影感、动画风、写实、赛博朋克）
- 示例：「电影感镜头，一位女孩在樱花树下缓缓转身，逆光，浅景深，4K画质」
