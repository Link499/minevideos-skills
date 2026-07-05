# Superpowers Skill 学习笔记

> 来源：clawhub `superpowers` (adapted from obra/superpowers)
> 学习时间：2026-07-05

---

## 核心理念

> **Spec-first, TDD, subagent-driven software development workflow**
> 每个编码任务都走 pipeline，"太简单不需要设计" 永远是错的。

---

## The Pipeline

```
Idea → Brainstorm → Plan → Subagent-Driven Build (TDD) → Code Review → Finish Branch
```

---

## Phase 1: Brainstorming

**硬门：不写任何代码，直到设计被批准！**

1. 探索项目上下文（文件、文档、最近提交）
2. 一次只问一个问题，偏好多选题
3. 提出 2-3 个方案 + 权衡 + 推荐
4. 分段展示设计，每段确认后继续
5. 写设计文档 → `docs/plans/YYYY-MM-DD-<topic>-design.md` → 提交
6. 交接给 Phase 2

---

## Phase 2: Writing Plans

- 每个任务 = 2-5 分钟：写测试 → 看失败 → 实现 → 看通过 → 提交
- 保存到 `docs/plans/YYYY-MM-DD-<feature>.md`
- 提供两种执行模式：
  - **Subagent-driven**：`sessions_spawn` 每个任务 + 两阶段审查
  - **Manual**：用户自己执行

---

## Phase 3: Subagent-Driven Development

**每个任务的循环：**
1. `sessions_spawn` 实现者（含任务+计划上下文）
2. `sessions_spawn` 规格审查者（确认代码匹配规格）
3. `sessions_spawn` 代码质量审查者（DRY/YAGNI/命名/错误处理）
4. 修复问题，必要时重新审查
5. 标记完成，进入下一个任务

**Dispatch 模式：**
```
Goal: [一句话]
Context: [计划文件路径]
Files: [精确路径]
Constraints: [不做什么 - TDD only, no scope creep]
Verify: [测试命令 + 预期输出]
Task: [完整任务文本]
```

---

## Phase 4: Systematic Debugging

**硬门：没有根因调查就不修 bug！**

四阶段：
1. **根因调查** — 读错误、复现、检查变更、追踪数据流
2. **模式分析** — 找正常工作的代码，对比差异
3. **假设+测试** — 一次一个假设，设计最小测试验证
4. **修复+验证** — 修根因不修症状，写回归测试

---

## Phase 5: Finishing Branch

1. 验证所有测试通过
2. 确定基础分支
3. 提供 4 个选项：本地合并 / 推送+PR / 保留 / 丢弃
4. 执行选择

---

## TDD 铁律

```
没有失败测试就不写生产代码！
先写了代码？删掉。重新开始。没有例外。
```

**Red-Green-Refactor：**
1. RED — 写一个最小的失败测试
2. 验证 RED — 确认测试失败（必须！）
3. GREEN — 写最简单的代码让测试通过
4. 验证 GREEN — 确认所有测试通过（必须！）
5. REFACTOR — 清理（不在此时加功能）

---

## 核心原则

- 一次只问一个问题
- TDD 永远
- YAGNI — 从所有设计中移除不必要的功能
- DRY — 不重复
- 系统化优于临时性
- 证据优于声明
- 每次绿色测试后提交

---

## 与现有 Skill 的协同

| Skill | 协同点 |
|-------|--------|
| **product-design** | Superpowers 的 Brainstorm 阶段可整合 PD 的需求分析方法 |
| **ui-ux-pro-max** | 设计文档阶段可调用 UI/UX 推理引擎 |
| **taste-skill** | 前端实现阶段应用 Anti-Slop 设计原则 |
| **website-replicate** | 如果是复刻项目，Superpowers 管流程，website-replicate 管执行 |
