# MineVideos Skills Collection 🎬

AI agent skills for the MineVideos project and general-purpose agent workflows.

## Skills Overview

### 🎬 MineVideos Core

| Skill | Description | Type |
|-------|-------------|------|
| **minevideos-generator** | AI视频生成 (T2V/I2V/R2V)，基于火山引擎 Seedance | 核心产品 |
| **minevideos-knowledge-graph** | MineVideos 领域知识图谱 | 领域知识 |
| **minevideos-vision** | MineVideos 产品愿景 | 产品规划 |

### 🎨 Design & UX

| Skill | Description | Source |
|-------|-------------|--------|
| **ui-ux-pro-max** | 67种风格 + 161配色 + 57字体 + 100推理规则 | [clawhub](https://clawhub.ai) |
| **ui-ux-pro-max-cn** | 中文UI/UX规范：字体、行高、行业配色、小程序 | [clawhub](https://clawhub.ai) |
| **product-design-gungun** | 产品设计：需求分析、PRD、原型、评审、A/B测试 | [clawhub](https://clawhub.ai) |

### 💻 Development

| Skill | Description | Source |
|-------|-------------|--------|
| **superpowers** | Spec-first, TDD, subagent-driven 开发流程 (6个参考文档) | [clawhub](https://clawhub.ai) |
| **critical-code-review** | 批判性代码审查：安全/架构/性能/模式 | local |
| **codebase-memory-mcp** | 代码库知识图谱 MCP (158种语言, 14个工具) | local |

### 🔍 Research & Communication

| Skill | Description | Source |
|-------|-------------|--------|
| **agent-reach** | 搜索14+平台 (Twitter/Reddit/YouTube/B站/小红书等) | local |
| **chat-req-first** | 聊天式需求探索工作流 | local |

## Design → Dev Chain

```
需求探索:  chat-req-first / product-design
    ↓
设计决策:  ui-ux-pro-max (风格/配色) + ui-ux-pro-max-cn (中文)
    ↓
开发流程:  superpowers (Brainstorm → Plan → TDD → Review)
    ↓
代码审查:  critical-code-review / codebase-memory-mcp
    ↓
市场调研:  agent-reach (全网搜索)
```

## Directory Structure

```
minevideos-skills/
├── minevideos-generator/     # AI视频生成核心
├── minevideos-knowledge-graph/
├── minevideos-vision/
├── ui-ux-pro-max/            # 含 data/ (CSV), assets/, scripts/
├── ui-ux-pro-max-cn/
├── product-design-gungun/
├── superpowers/              # 含 references/ (6个文档)
├── critical-code-review/
├── codebase-memory-mcp/
├── agent-reach/
├── chat-req-first/
└── memory/                   # 学习笔记
    ├── product-design-notes.md
    ├── superpowers-notes.md
    ├── ui-ux-pro-max-notes.md
    ├── taste-skill-notes.md
    └── vibe-coding-notes.md
```

## Related Repos

- [minevideos](https://github.com/Link499/minevideos) — 主项目
- [minevideos-backend](https://github.com/Link499/minevideos-backend) — 后端
- [minevideos-skill](https://github.com/Link499/minevideos-skill) — 单独的视频生成 skill (已合并至此)
