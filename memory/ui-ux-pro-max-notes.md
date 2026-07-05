# UI/UX Pro Max 学习笔记

> 来源：ui-ux-pro-max-skill (97K⭐ GitHub) + 中文本地化版 (拾珍小栈)
> 整理时间：2026-07-04

---

## 一、这是什么？

一个给 AI 编程助手用的**设计智能系统**，核心思路是：

> 不要让 AI 瞎猜设计，给它行业规则、风格数据库、配色方案、字体搭配，
> 让它像有经验的设计师一样做决策。

### 核心数据资产

| 维度 | 数量 | 说明 |
|------|------|------|
| UI 风格 | 67种 | 从极简主义到液态玻璃 |
| 配色方案 | 161种 | 行业适配 |
| 字体搭配 | 57组 | 含中文字体 |
| 技术栈 | 22种 | React/Vue/小程序等 |
| 推理规则 | 100条 | 行业→风格→配色→字体的决策链 |
| UX 规范 | 99条 | 含反模式 |

---

## 二、核心方法论：推理引擎

### 决策流程

```
用户请求："做一个美容Spa的落地页"
        ↓
① 行业匹配 → 美容/Spa → 找到行业规则
        ↓
② 风格推荐 → Soft UI Evolution（柔和深度、有机形状）
        ↓
③ 配色选择 → 柔粉#E8B4B8 + 鼠尾草绿#A8D5BA + 金色CTA#D4AF37
        ↓
④ 字体搭配 → Cormorant Garamond / Montserrat
        ↓
⑤ 布局模式 → Hero-Centric + Social Proof
        ↓
⑥ 反模式过滤 → 禁止：荧光色、暴力动画、暗色模式、AI紫粉渐变
        ↓
⑦ 交付检查 → 对比度/焦点态/响应式/减动画偏好
```

### 每条推理规则包含

| 字段 | 示例（SaaS通用） |
|------|-----------------|
| 推荐布局 | Hero + Features + CTA |
| 风格优先级 | 玻璃拟态 + 扁平设计 |
| 色彩情绪 | 信任蓝 + 对比强调色 |
| 排版情绪 | 专业 + 层次感 |
| 关键效果 | 微妙 hover(200-250ms) + 平滑过渡 |
| 决策规则 | 如果侧重UX→优先极简；如果数据密集→加玻璃拟态 |
| 反模式 | 过度动画、默认暗色模式 |

---

## 三、与电影感/Vibe Coding 的结合点

### 3.1 电影感 = 多风格叠加

根据 ui-ux-pro-max 的数据，电影感网页是以下风格的组合：

| 风格 | 贡献 | 关键效果 |
|------|------|---------|
| Aurora UI | 极光渐变背景 | 流动渐变 + 8-12s动画 + 色彩层次 |
| Glassmorphism | 玻璃质感面板 | backdrop-blur(10-20px) + 半透明边框 |
| Liquid Glass | 液态玻璃动效 | 形态变化 + 流体动画(400-600ms) + 色差 |
| Parallax Storytelling | 叙事性视差 | 3-5层滚动 + scroll-triggered + 电影感 |
| Kinetic Typography | 动态文字 | GSAP ScrollTrigger + split text + typing |
| Hero-Centric | 首屏冲击力 | 全宽Hero + 60-80字标题 + CTA脉冲 |
| Motion-Driven | 全局动效 | Intersection Observer + 300-400ms hover |
| Gradient Mesh | 极光进化 | 多色网格渐变 + 流动变色 + 多点stop |

### 3.2 电影感配色速查

从 ui-ux-pro-max 数据中提取：

**暗色系电影感：**
- 主色：#0A0A0A（深黑）→ #1A1A1A（卡片）
- 强调：#C9A96E（金色）→ #D4AF37（深金）
- 文字：#F5F5F5（主）→ #A0A0A0（辅）→ #666666（弱）

**Aurora 配色：**
- Electric Blue #0080FF + Magenta #FF1493
- 互补：Blue-Orange, Purple-Yellow

**Gradient Mesh：**
- Cyan #00FFFF + Magenta #FF00FF + Yellow #FFFF00 + Blue #0066FF

### 3.3 电影感动效规范

| 效果 | 时长/参数 | 工具 |
|------|----------|------|
| 滚动渐入 | 0.8s ease-out | Intersection Observer / GSAP ScrollTrigger |
| Hover 微交互 | 200-300ms | CSS transition |
| 视差滚动 | 3-5层 | translateY(scroll) |
| 粒子背景 | 60fps | Canvas API |
| 流体渐变 | 8-12s infinite | CSS @keyframes |
| 形态变化 | 400-600ms curves | SVG morph / CSS |
| 文字动画 | split + stagger 0.2s | GSAP SplitText |

---

## 四、关键设计规则

### 4.1 通用交付检查清单

- [ ] 无 emoji 作为图标（用 SVG: Heroicons/Lucide）
- [ ] 所有可点击元素有 cursor: pointer
- [ ] Hover 状态平滑过渡（150-300ms）
- [ ] 亮色模式文字对比度 ≥ 4.5:1
- [ ] 键盘导航焦点可见
- [ ] 尊重 prefers-reduced-motion
- [ ] 响应式：375px, 768px, 1024px, 1440px

### 4.2 反模式清单（按行业）

| 行业 | ❌ 禁止 |
|------|--------|
| 金融 | 花哨渐变、不安全感设计、红色用于亏损 |
| 电商 | 大面积暗色、纯英文导航 |
| SaaS | 过度动画、默认暗色模式 |
| 教育 | 花哨动画干扰学习、深色背景 |
| 政务 | 花哨效果、不正式表达 |
| 美容/奢华 | 荧光色、暴力动画、AI紫粉渐变 |

### 4.3 中文专属规则

- 中文字体 fallback 栈：`"PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif`
- 中文行高 ≥ 1.6（比英文需要更大行高）
- CTA 按钮用中文
- 数字字体与中文协调
- 按钮圆角：8px（常规）/ 20px（胶囊）
- 列表项高度 ≥ 44px（手指友好）

---

## 五、与我们现有 Skill 的整合

### ui-ux-pro-max + website-replicate 的协同

```
用户："复刻这个电影感网站"
        ↓
website-replicate 负责：收集 → 判断 → 编码
        ↓
ui-ux-pro-max 在"判断"阶段提供：
  - 风格识别（这是哪种风格组合？）
  - 配色提取验证（提取的颜色对不对？）
  - 字体搭配建议
  - 反模式检查
  - 交付前清单验证
```

### 协同流程

1. **Phase 1 收集** → website-replicate 主导
2. **Phase 2 判断** → ui-ux-pro-max 提供设计智能
   - 识别目标网站属于哪些风格
   - 推荐配色/字体/效果组合
   - 过滤反模式
3. **Phase 3 编码** → website-replicate 主导
4. **验证** → ui-ux-pro-max 的检查清单做最终验证

---

## 六、关键洞察

1. **设计决策可以系统化** — 不是"感觉好看"，是行业规则+风格匹配+反模式过滤
2. **67种风格足够覆盖绝大多数需求** — 关键是选对组合，不是从头发明
3. **反模式比正模式更重要** — "不要做什么"比"要做什么"更清晰
4. **推理引擎 > 模板** — 不是套模板，是根据条件做决策
5. **中文产品有独特规则** — 字体、配色、行高、交互尺寸都不同
6. **与 vibe coding 完美互补** — vibe coding 负责"快速出活"，ui-ux-pro-max 负责"出对活"
