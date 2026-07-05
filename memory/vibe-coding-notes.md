# Vibe Coding 学习笔记

> 来源：Andrej Karpathy 原始推文、Simon Willison 博客、虎鲸碎碎念、设计师言炎
> 整理时间：2026-07-04

---

## 一、什么是 Vibe Coding

### 原始定义（Andrej Karpathy，2025年2月6日）

> There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.

**核心特征：**
- 完全交给感觉（vibes），拥抱指数级增长
- 忘记代码的存在——我"看到东西、说出东西、运行东西、粘贴东西，大部分时候能用"
- 用语音（SuperWhisper）跟 Cursor Composer 说话，几乎不碰键盘
- 说"最蠢的话"比如"把侧边栏 padding 减一半"，因为懒得自己找
- 永远点 "Accept All"，不再看 diff
- 遇到报错直接复制粘贴进去，通常就好了
- 代码超出理解范围，有时修不了 bug 就绕过去

**Karpathy 的定位：** 这是周末废弃项目用的，不是生产级编码。但它很好玩。

### Simon Willison 的澄清

> **Vibe coding ≠ 所有 AI 辅助编程**

关键区分：
- Vibe Coding = 不审阅 LLM 写的代码就接受
- 负责任的 AI 编程 = 审阅、测试、确保自己能解释代码

> "I won't commit any code to my repository if I couldn't explain exactly what it does to somebody else."

---

## 二、Vibe Coding 的设计哲学

### 2.1 从"写代码"到"提需求"

传统编程：**思考 → 设计 → 编码 → 测试**
Vibe Coding：**说想要什么 → 看效果 → 说不满意 → 重复**

这不是偷懒，是范式的转变：
- 人负责**品味和判断**（"这个感觉不对"）
- AI 负责**实现和迭代**（"好我改一版"）
- 交互模式从键盘变成**对话**

### 2.2 "See, Say, Run, Paste"

Karpathy 的四步循环：

```
See（看到效果）
  ↓
Say（说出想要什么）
  ↓
Run（运行看结果）
  ↓
Paste（遇到报错就粘贴进去）
  ↓
重复
```

没有"读代码"这一步。没有"理解架构"这一步。
这是 bug 还是 feature？取决于场景。

### 2.3 品味 > 技术

Vibe coding 的核心竞争力不是你会不会写代码，而是：
- **你知道什么是好的**（审美、品味、用户体验直觉）
- **你能清晰描述你想要的**（prompt engineering）
- **你能快速判断结果的好坏**（evaluation skill）

这解释了为什么设计师和产品经理往往比程序员更适合 vibe coding——他们本来就不写代码，但他们知道什么是好的。

---

## 三、Vibe Coding 的最佳实践

### 3.1 适合的场景 ✅

| 场景 | 为什么适合 |
|------|-----------|
| 周末项目 / 原型 | 低风险，快速验证想法 |
| 学习和探索 | 最好的学习是动手做 |
| 一次性工具 | 用完即弃，不需要维护 |
| 可视化 / 创意项目 | 效果直观，好坏一眼看 |
| 个人工具 | 只自己用，出 bug 无伤大雅 |

### 3.2 不适合的场景 ❌

| 场景 | 为什么不适合 |
|------|------------|
| 生产系统 | 安全、可靠性要求高 |
| 涉及密码/密钥 | 不理解代码可能导致泄露 |
| 处理隐私数据 | 数据可能意外离开本机 |
| 涉及付费 API | 可能产生高额账单 |
| 被其他人使用的工具 | 你是唯一能修 bug 的人 |

### 3.3 安全底线

Simon Willison 的安全检查清单：
- 📋 **评估风险**：如果出 bug 会造成什么伤害？
- 🔐 **注意密钥**：任何看起来像密码的东西都要小心
- 🔒 **数据隐私**：如果涉及你不想屏幕共享的数据，要特别谨慎
- 💰 **费用控制**：接入付费 API 一定要设 billing limit
- 🌐 **网络公民**：不要让你的工具给别人增加负载
- 🤝 **求助确认**：如果做给别人用的，找有经验的人 review

### 3.4 沙盒优先

Claude Artifacts 的沙盒设计是 vibe coding 的理想环境：
- 代码运行在锁定的 `<iframe>` 里
- 只能加载批准的库
- 不能发网络请求到其他站点
- 几乎不可能"搞砸"

---

## 四、Vibe Coding 与 Skill 的关系

### 4.1 Skill = 给 Vibe Coding 加结构

纯 vibe coding 的问题是：**太依赖感觉，没有方法**。

虎鲸碎碎念的洞察：
> Agent 经常写错代码，不是模型不够强，而是太早开始猜。

解决方案 = **Skill**：
- 把"感觉"变成"流程"
- 把"猜"变成"侦察→判断→行动"
- 但保留 vibe coding 的核心优势：快速迭代、效果驱动

### 4.2 设计师言炎的补充

> 拼的不是你有没有用到最新模型，真正有用的是流程。

他的流程：
1. 先定 Landing Page 的参考结构
2. 再备好素材（人物、流体、动态视频）
3. 先跑出网站骨架
4. 再按 section 一块块替进去修质感

这本质上就是**结构化的 vibe coding**：
- 保留"先看效果"的快速反馈循环
- 加入"先准备后动手"的纪律

### 4.3 Simon Willison 的方法论

> Context is king. —— 管理好上下文是获得好结果的关键。

他的实践原则：
1. **设合理期望** — LLM 是过度自信的结对编程搭档
2. **考虑训练截止日期** — 选库时优先选稳定、流行的
3. **上下文为王** — 管理对话上下文，卡住了就重开
4. **先问选项** — "有哪些方案？给我示例"
5. **精确指令** — 明确告诉它做什么
6. **必须测试** — 写完一定要跑
7. **当对话来用** — 从简单版本开始，逐步迭代
8. **用能运行代码的工具** — Claude Code、Cursor 等
9. **准备好接管** — 卡住时人要能接手
10. **LLM 放大已有专业能力** — 越懂的人用得越好

---

## 五、Vibe Coding 的设计模式

### 5.1 渐进式构建（Progressive Building）

```
第1轮：最简版本 → 跑通 → 确认方向
第2轮：加细节 → 跑通 → 修正方向
第3轮：打磨质感 → 跑通 → 微调
```

不要一上来就要完美版本。先跑，再改。

### 5.2 效果驱动开发（Effect-Driven Development）

```
传统：想功能 → 写代码 → 看效果
Vibe：描述效果 → AI 写代码 → 看效果 → 调描述
```

用效果描述替代功能描述：
- ❌ "实现一个轮播图组件"
- ✅ "我要一个全屏的图片轮播，每张图3秒自动切换，底部有金色进度条，hover 时暂停"

### 5.3 参考驱动（Reference-Driven）

```
不要说"做一个好看的网站"
要说"像 Apple 的产品页，暗色系，电影感，用金色强调"
```

给 AI 参考 > 给 AI 规则。因为 AI 对"好看"的理解和你不一样，但它能模仿具体的风格。

### 5.4 分区迭代（Section-by-Section）

设计师言炎的方法：**先骨架，再一块块替换修质感**

```
Step 1：整体骨架（布局 + 占位内容）
Step 2：Hero Section 精修
Step 3：About Section 精修
Step 4：Features Section 精修
...
```

比一次性全做完高效得多。因为：
- 每步可验证
- 上下文更聚焦
- 出问题容易定位

---

## 六、关键洞察总结

1. **Vibe Coding 是一种范式，不是一种技术** — 从"写代码"到"提需求+审效果"
2. **品味 > 技术** — 知道什么是好的，比知道怎么写更重要
3. **低风险场景放开了干，高风险场景要审阅** — 别把所有 AI 编程都叫 vibe coding
4. **Skill 是 vibe coding 的纪律** — 保留速度优势，加入方法论
5. **Context is King** — 管理好上下文，大部分问题迎刃而解
6. **先跑再改** — 渐进式构建 > 一次性完美
7. **给参考，别给规则** — "像 Apple 官网" > "现代简约风格"
8. **效果驱动** — 用你想要的效果来描述需求
9. **沙盒优先** — 安全的实验环境让 vibe coding 更自由
10. **LLM 放大已有能力** — 你越懂，它越强

---

## 七、推荐资源

- [Karpathy 原始推文](https://twitter.com/karpathy/status/1886192184808149383) — vibe coding 的诞生
- [Simon Willison: Not all AI-assisted programming is vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/) — 最清醒的解读
- [Simon Willison: How I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) — 实战方法论
- 虎鲸碎碎念（抖音 jz_ai_skills）— Skill 驱动的网站复刻
- 设计师言炎（抖音）— 电影感建站流
