# Taste Skill 学习笔记

> 来源：clawhub `@akdira/taste-skill` (Anti-Slop Frontend Skill)
> 注：`@kehaoc/taste-skill` 是 Skill 市场工具（发现/安装/发布 skill），定位不同
> 学习时间：2026-07-05

---

## 核心理念

> **Anti-Slop：让 AI 生成的页面看起来不像 AI 生成的。**
> 大多数 LLM 设计输出很烂，因为模型跳到默认美学，而不是读懂需求。

---

## 0. Brief Inference（读懂需求再动手）

### 读取信号
1. **页面类型** — Landing / Portfolio / Redesign / Editorial
2. **氛围词** — "minimalist", "Linear-style", "Awwwards", "brutalist" 等
3. **参考信号** — 链接、截图、竞品品牌
4. **受众** — B2B采购 vs 设计敏感消费者 vs 猎头
5. **已有品牌资产** — Logo、色、字体、摄影
6. **隐性约束** — 无障碍优先、政务、监管行业

### 设计宣读（Design Read）
在写任何代码前，先声明一行：
> "Reading this as: `<page kind>` for `<audience>`, with a `<vibe>` language, leaning toward `<design system>`."

### 反默认纪律
**禁止默认使用：** AI紫渐变、深色mesh上的居中hero、三个等大feature卡片、通用glassmorphism、无限循环微动画、Inter + slate-900

---

## 1. 三旋钮（Core Configuration）

| 旋钮 | 基线 | 范围 |
|------|------|------|
| **DESIGN_VARIANCE** | 8 | 1=完美对称 → 10=艺术混乱 |
| **MOTION_INTENSITY** | 6 | 1=静态 → 10=电影级/物理 |
| **VISUAL_DENSITY** | 4 | 1=画廊/留白 → 10=驾驶舱/密排 |

### 场景预设

| 场景 | VARIANCE | MOTION | DENSITY |
|------|----------|--------|---------|
| SaaS Landing | 7 | 6 | 4 |
| Agency Landing | 9 | 8 | 3 |
| Premium Consumer | 7 | 6 | 3 |
| Designer Portfolio | 8 | 7 | 3 |
| Developer Portfolio | 6 | 5 | 4 |
| Editorial/Blog | 6 | 4 | 3 |
| 政务/信任优先 | 3 | 2 | 5 |

---

## 2. Brief → 设计系统映射

### 用正式设计系统（有官方包的场景）

| 场景 | 用什么 |
|------|--------|
| Microsoft/企业SaaS | Fluent UI |
| Google风格 | Material Web + M3 tokens |
| IBM风格B2B | Carbon |
| Shopify | Polaris |
| Atlassian | Atlaskit |
| GitHub风格 | Primer |
| 英国政务 | govuk-frontend |
| 美国政务 | USWDS |
| 现代SaaS | shadcn/ui |
| Tailwind系 | Tailwind v4 |

**诚实规则：** 有官方包就用官方包，不要手写CSS模拟。
**一个项目一个系统，不要混搭。**

### 美学方向（无官方包的场景）

用原生 CSS + Tailwind + 组件库实现，诚实标注借鉴 vs 官方。

| 美学 | 实现方式 |
|------|----------|
| Glassmorphism | `backdrop-filter` + 实心回退 |
| Bento | CSS Grid 混合尺寸 |
| Brutalism | 原生CSS + 等宽字体 |
| Editorial | 衬线体 + 非对称网格 |
| Dark Tech | 等宽 + 霓虹强调色 |
| Aurora | SVG/径向渐变层叠 |
| Apple Liquid Glass | 近似实现，标注为approximation |

---

## 3. 默认技术栈

- **框架：** React / Next.js (RSC优先)
- **样式：** Tailwind v4
- **动画：** Motion (原Framer Motion)，`import from "motion/react"`
- **字体：** `next/font` 自托管，不用 Google Fonts `<link>`
- **状态：** 连续值用 `useMotionValue`，不用 `useState`
- **图标：** Phosphor > hugeicons > Radix > Tabler；避免 lucide；禁止手写SVG图标

### 布局规则
- **绝不用** `h-screen`，**总是用** `min-h-[100dvh]`
- **绝不用** flex 百分比数学，**总是用** CSS Grid
- 容器 `max-w-[1400px] mx-auto`

---

## 4. 设计工程指令（偏差修正）

### 排版
- Display: `text-4xl md:text-6xl tracking-tighter leading-none`
- Body: `text-base text-gray-600 leading-relaxed max-w-[65ch]`
- **默认不选 Inter**，优先 Geist / Outfit / Cabinet Grotesk / Satoshi
- **衬线体极度不鼓励作为默认**，"创意=衬线" 是 AI 最大特征标记
- **特别禁止：** Fraunces 和 Instrument_Serif 作为默认
- **强调规则：** 用同字体的 italic/bold，不要混合字族强调

### 字体搭配
- Geist + Geist Mono
- Satoshi + JetBrains Mono
- Cabinet Grotesk + Inter Tight

---

## 与现有 Skill 的协同

| Skill | 协同点 |
|-------|--------|
| **superpowers** | Taste 在实现阶段指导前端设计决策 |
| **ui-ux-pro-max** | Taste 更偏"怎么避免模板化"，ui-ux 更偏"怎么选风格和配色" |
| **website-replicate** | 复刻时用 Taste 的 Design Read 来判断目标风格 |
| **liquid-glass-react** | Taste 明确说 Liquid Glass 是近似实现，这个skill提供具体实现 |
