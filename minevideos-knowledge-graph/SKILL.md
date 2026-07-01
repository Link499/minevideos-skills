# MineVideos 项目知识图谱

## 概述
MineVideos 是一个 AI 视频生成平台，包含完整的用户系统、视频生成 pipeline 和任务管理。

## 项目架构

### 前端
- 技术栈：React/Vue
- 功能：用户界面、视频预览、进度展示

### 后端
- 技术栈：Node.js/Express
- 功能：API 服务、用户认证、任务调度

### 视频生成服务
- 技术栈：AI Pipeline
- 功能：端到端视频生成、任务队列

## 团队角色

### @Eve - 全栈开发
- 负责：整体架构、前后端协调
- 职责：代码审查、技术决策

### @Pixel - 前端开发
- 负责：用户界面、交互体验
- 职责：前端优化、错误处理

### @Volt - 后端开发
- 负责：API 设计、数据库
- 职责：性能优化、安全配置

### @Forge - 安全监督
- 负责：安全审计、合规检查
- 职责：漏洞扫描、权限管理

## 核心功能

### 1. 用户注册/登录
- 功能：账号创建、身份验证
- 状态：存在 CORS 问题，失误率 50%

### 2. 端到端视频生成
- 功能：AI 驱动的视频生成
- 状态：流程中断，失误率 50%

### 3. 任务状态追踪
- 功能：实时进度监控
- 状态：需要完善

## 已知问题

### 🔴 严重：CORS 配置冲突
**问题描述：**
```javascript
// 错误配置
app.use(cors({
  origin: '*',
  credentials: true
}))
```

**影响：**
- 浏览器拒绝通配符 origin + credentials 组合
- 前端请求被拦截
- 登录功能完全不可用

**修复方案：**
```javascript
// 正确配置
app.use(cors({
  origin: ['http://localhost:3000', 'https://yourdomain.com'],
  credentials: true
}))
```

### 🟡 中等：前端连接失败
**问题描述：**
- 前端返回状态码 000
- 网络请求失败但无错误处理

**影响：**
- 用户看到空白页面
- 无法区分错误类型

**修复方案：**
- 添加统一错误处理
- 分类处理网络错误、CORS 错误、业务错误

### 🟡 中等：视频生成中断
**问题描述：**
- 任务启动后无状态追踪
- 失败时无法恢复

**影响：**
- 用户不知道进度
- 资源浪费

**修复方案：**
- 实现任务状态管理
- 添加进度轮询机制
- 实现失败重试

## 失误率分析

### 当前状态
| 功能模块 | 失误率 | 状态 |
|---------|--------|------|
| 注册/登录 | 50% | CORS 问题 |
| 视频生成 | 50% | 流程中断 |
| **总体** | **50%** | 需紧急修复 |

### 目标状态
| 功能模块 | 目标失误率 | 改进措施 |
|---------|-----------|---------|
| 注册/登录 | <5% | 修复 CORS + 错误处理 |
| 视频生成 | <10% | 完善任务管理 |
| **总体** | **<5%** | 全面修复 + 测试 |

### 预期改进
- 修复 CORS → 消除 50% 登录失败
- 完善错误处理 → 提升用户体验
- 任务管理完善 → 降低视频生成失败率
- **总体改进：失误率从 50% 降至 <5%**

## 改进计划

### 第一阶段：紧急修复（1-2天）
- [ ] 修复 CORS 配置 - @Volt
- [ ] 完善前端错误处理 - @Pixel
- [ ] 添加健康检查端点 - @Volt

### 第二阶段：功能完善（3-5天）
- [ ] 完善视频生成任务管理 - @Eve
- [ ] 添加日志系统 - @Volt
- [ ] 编写端到端测试 - @Pixel

### 第三阶段：质量提升（1-2周）
- [ ] 添加 API 文档 - @Pixel
- [ ] 单元测试覆盖率 80%+ - 全员
- [ ] 性能优化 - @Forge

## 成功模式

### 模式 1：异步任务管理
**应用场景：** 视频生成、文件处理
**复用价值：** 高
**核心代码：**
```javascript
class TaskManager {
  createTask(type, params) {
    const taskId = uuidv4();
    this.tasks.set(taskId, {
      id: taskId,
      status: 'pending',
      progress: 0,
      createdAt: Date.now()
    });
    return taskId;
  }
  
  async pollStatus(taskId) {
    return setInterval(async () => {
      const task = this.tasks.get(taskId);
      if (task.status === 'completed') {
        clearInterval(interval);
      }
    }, 2000);
  }
}
```

### 模式 2：统一错误处理
**应用场景：** 所有 API 请求
**复用价值：** 高
**核心代码：**
```javascript
async function apiRequest(url, options = {}) {
  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    if (error.message === 'Failed to fetch') {
      throw new Error('网络连接失败');
    }
    throw error;
  }
}
```

### 模式 3：健康检查
**应用场景：** 所有后端服务
**复用价值：** 中
**核心代码：**
```javascript
app.get('/health', async (req, res) => {
  const checks = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    checks: {}
  };
  
  try {
    await db.ping();
    checks.checks.database = 'ok';
  } catch (error) {
    checks.status = 'unhealthy';
  }
  
  res.json(checks);
});
```

## 技术栈总结

### 前端
- React/Vue
- Fetch API
- 状态管理

### 后端
- Node.js
- Express
- CORS 中间件
- SQLite/PostgreSQL

### 视频生成
- AI Pipeline
- 任务队列
- 进度追踪

### 部署
- GitHub
- 自动化测试
- 健康检查

## 关键指标

- **当前失误率：** 50%
- **目标失误率：** <5%
- **改进幅度：** 90%
- **预计完成时间：** 2 周

## 下一步行动

1. **立即修复 CORS 配置**（今天）
2. **完善错误处理**（明天）
3. **添加健康检查**（今天）
4. **完善任务管理**（3天内）
5. **编写测试**（5天内）

## 相关文件

- 知识图谱：`MineVideos_知识图谱.drawio`
- 代码审查报告：`REVIEW.md`
- 工作日志：`memory/2026-07-01.md`
