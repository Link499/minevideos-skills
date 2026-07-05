# MineVideos AI 视频生成技能

基于火山引擎 Seedance 大模型的 AI 视频生成 Coze Skill。

## ✨ 功能

| 模式 | 说明 | 输入 |
|------|------|------|
| **T2V** | 文本生视频 | 文字描述 |
| **I2V** | 图片生视频 | 图片URL + 描述 |
| **R2V** | 参考视频生视频 | 参考视频URL + 描述 |

## 🚀 快速开始

### 1. 安装到 Coze

在 [Coze 技能商店](https://www.coze.cn) 搜索 `MineVideos AI视频生成` 并安装。

### 2. 配置凭证

首次使用需要配置火山引擎 API Key：

1. 前往 [火山引擎控制台](https://console.volcengine.com/ark) 获取 API Key
2. 在技能设置页面填入 API Key

### 3. 使用

```bash
# 文本生视频
python main.py --mode t2v --prompt "电影感镜头，一位女孩在樱花树下缓缓转身，逆光，浅景深"

# 图片生视频
python main.py --mode i2v --prompt "图片中的人物缓缓转身微笑" --image_url "https://example.com/photo.jpg"

# 查询任务状态
python main.py --query --task_id "xxx"

# 等待任务完成
python main.py --wait --task_id "xxx" --max_wait 600
```

## 🏗️ 架构设计

灵感来源于 [DSA (Daily Stock Analysis)](https://github.com/ZhuLinsen/daily_stock_analysis) 的模块化设计：

```
minevideos-generator/
├── SKILL.md          # 技能指令（触发条件 + 工作流程 + 输出格式）
├── main.py           # 核心脚本（API调用 + 任务管理 + 结果查询）
├── requirements.txt  # 依赖声明
├── README.md         # 本文档
└── .env.example      # 环境变量模板
```

### 设计模式借鉴

- **SKILL.md 定义接口**：参考 DSA 的函数签名 + 输入/输出 + 示例模式
- **统一配置入口**：参考 DSA 的 Config 类设计，所有 API Key 通过凭证系统统一管理
- **结构化输出**：参考 DSA 的 AnalysisResult，VideoResult 包含任务状态、视频URL、封面等
- **模型降级策略**：fast 模型失败自动降级到 standard，类似 DSA 的多数据源降级

## 📄 License

MIT © 2026 Links / MineVideos AI
