# Impeccable UX/UI 学习笔记

**日期**: 2025-07-05
**来源**: [clawhub/maryambahri/impeccable-uxui](https://clawhub.ai/maryambahri/impeccable-uxui)
**原作者**: Paul Bakaus ([@pbakaus](https://twitter.com/nickerbocker))
**官网**: [impeccable.style](https://impeccable.style)
**GitHub**: [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable)
**许可**: MIT-0

## 核心定位

**反 AI 模板设计技能** — 让 AI 生成的前端不再是千篇一律的 "AI slop"。

## 7 大领域参考

| 领域 | 核心要点 |
|------|---------|
| **Typography** | 模数化字号系统（5级足够）、用 clamp() 流体字号、避开 Inter/Roboto、配对原则 |
| **Color & Contrast** | OKLCH 色彩空间、中性色偏品牌色调、禁止纯黑/纯白、禁止 cyan-on-dark AI配色 |
| **Spatial Design** | 节奏化间距、不对称布局、fluid spacing、打破网格制造焦点 |
| **Motion Design** | 指数缓动(ease-out-quart)、用 transform/opacity 不用 layout 属性、grid-template-rows 做高度动画 |
| **Interaction Design** | 乐观UI、渐进式披露、空状态教用户、不要重复信息 |
| **Responsive Design** | 容器查询 @container、适配不要截肢、移动端不藏功能 |
| **UX Writing** | 错误信息三要素(发生了什么+为什么+怎么修)、禁止怪用户、术语一致性 |

## 20 个 Steering Commands

/audit, /critique, /polish, /distill, /animate, /palette, /typography, /layout, /spacing, /responsive, /accessibility, /contrast, /components, /icons, /motion, /copy, /tone, /voice, /empty-states, /forms

## AI Slop 测试

> 把界面给某人看，说"AI做的"，对方会信吗？信了就是问题。
> 好的界面应该让人问"这是怎么做的？"而不是"这是哪个AI做的？"

## 反模式清单（关键！）

- ❌ Inter/Roboto/Arial 字体
- ❌ cyan-on-dark、purple-to-blue 渐变、neon accents
- ❌ 渐变文字做"冲击感"
- ❌ 万物皆卡片、卡片套卡片
- ❌ 同尺寸卡片网格（icon + heading + text 无限重复）
- ❌ Hero 大数字 + 小标签 + gradient accent
- ❌ 一切居中
- ❌ Glassmorphism 装饰性滥用
- ❌ sparkline 装饰
- ❌ bounce/elastic 缓动
- ❌ 模态框作为默认方案

## 与其他 Design Skill 的关系

| Skill | 角色差异 |
|-------|---------|
| **impeccable-uxui** | 质量守门人 — 审查/打磨已有设计，消除 AI 痕迹 |
| **ui-ux-pro-max** | 数据驱动 — 67风格+161配色+57字体的参数化设计系统 |
| **ui-ux-pro-max-cn** | 中文规范 — 本土化行高、字体、行业配色 |
| **product-design-gungun** | 流程驱动 — 需求→PRD→原型→评审 |

**推荐组合**: ui-ux-pro-max (选风格/配色) → impeccable-uxui (审查反模式) → 最终交付

## Context Gathering Protocol

设计前必须确认:
1. 目标受众（谁用？什么场景？）
2. 用例（他们想完成什么？）
3. 品牌个性/调性（界面应该什么感觉？）

来源优先级: 已加载指令 → `.impeccable.md` → 运行 teach-impeccable

## 设计方向选择

选一个**大胆**的美学方向：
- 极简主义 / 极繁主义 / 复古未来 / 有机自然 / 奢华精致
- 俏皮玩具 / 编辑杂志 / 粗野主义 / 装饰艺术 / 柔和粉彩
- 工业实用 / ... 自定义

**关键**: 大胆极繁和精致极简都行——重要的是**意图性**，不是强度。
