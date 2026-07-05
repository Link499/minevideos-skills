# Critical Code Review Skill

## 概述
用批判性思维审查代码，发现潜在问题，提供改进建议，并将成功模式打包成可复用组件。

## 触发场景
- 用户要求审查代码
- 需要分析项目架构
- 排查系统性问题
- 优化代码质量
- 降低失误率

## 核心流程

### 1. 架构层面批判

#### 1.1 安全性审查
```
检查清单：
□ CORS 配置是否正确（不能用 * + credentials）
□ 是否有硬编码的密钥/密码
□ API 端点是否有认证保护
□ 敏感数据是否加密传输
□ 是否有 SQL 注入/XSS 风险
```

**真实案例：CORS 配置冲突**
```javascript
// ❌ 错误示例
app.use(cors({
  origin: '*',
  credentials: true  // 浏览器会拒绝这个组合
}))

// ✅ 正确示例
app.use(cors({
  origin: ['http://localhost:3000', 'https://yourdomain.com'],
  credentials: true
}))
```

#### 1.2 错误处理审查
```
检查清单：
□ 是否有统一的错误处理中间件
□ 前端是否正确处理网络错误（状态码 0）
□ 是否有超时机制
□ 是否有重试逻辑
□ 错误信息是否对用户友好
```

**真实案例：前端状态码 000**
```javascript
// ❌ 错误示例
fetch('/api/login', { credentials: 'include' })
  .then(res => res.json())  // 网络错误时这里会崩溃

// ✅ 正确示例
fetch('/api/login', { credentials: 'include' })
  .then(res => {
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  })
  .catch(err => {
    if (err.message === 'Failed to fetch') {
      // 网络错误，可能是 CORS 问题
      showError('网络连接失败，请检查网络设置');
    } else {
      showError('登录失败，请重试');
    }
  });
```

#### 1.3 端到端流程审查
```
检查清单：
□ 关键流程是否有完整的链路追踪
□ 异步任务是否有状态查询机制
□ 长时间任务是否有进度反馈
□ 失败任务是否有重试/恢复机制
□ 是否有端到端自动化测试
```

**真实案例：视频生成流程中断**
```javascript
// ❌ 错误示例
const taskId = await startVideoGeneration(params);
// 没有轮询机制，不知道任务是否完成

// ✅ 正确示例
const taskId = await startVideoGeneration(params);
const pollInterval = setInterval(async () => {
  const status = await checkTaskStatus(taskId);
  updateProgress(status.progress); // 10%, 50%, 100%
  
  if (status.completed) {
    clearInterval(pollInterval);
    showSuccess('视频生成完成');
  } else if (status.failed) {
    clearInterval(pollInterval);
    showError(`生成失败: ${status.error}`);
  }
}, 2000);
```

### 2. 代码质量批判

#### 2.1 代码重复检测
```bash
# 使用 jscpd 检测重复代码
npx jscpd src/

# 重复率标准：
# < 5%  : 优秀
# 5-10% : 良好
# 10-20%: 需要改进
# > 20% : 必须重构
```

#### 2.2 复杂度分析
```bash
# 使用 eslint 检查复杂度
npx eslint --rule '{"complexity": ["error", 10]}' src/

# 复杂度标准：
# 1-5   : 简单，易维护
# 6-10  : 中等，可接受
# 11-20 : 复杂，建议拆分
# > 20  : 高度复杂，必须重构
```

#### 2.3 依赖审查
```bash
# 检查过时依赖
npm outdated

# 检查安全漏洞
npm audit

# 检查未使用依赖
npx depcheck
```

### 3. 失误率分析与降低策略

#### 3.1 失误率计算公式
```
失误率 = 失败次数 / 总尝试次数 × 100%

按功能模块分类：
- 注册/登录失误率
- 核心功能失误率
- 端到端流程失误率
```

#### 3.2 降低失误率的 5 个策略

**策略 1：前置测试**
```
部署前必须通过的测试：
1. 单元测试覆盖率 > 80%
2. 集成测试覆盖所有关键路径
3. 端到端测试覆盖核心功能
4. 性能测试验证响应时间
```

**策略 2：自动化健康检查**
```bash
#!/bin/bash
# deploy-check.sh

# 检查后端健康
curl -f http://localhost:8080/health || exit 1

# 检查前端可访问
curl -f http://localhost:3000 || exit 1

# 检查 CORS 配置
curl -I -X OPTIONS http://localhost:8080/api \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" | \
  grep "access-control-allow-origin" || exit 1

# 检查核心功能
curl -f http://localhost:8080/api/status || exit 1

echo "✓ 所有检查通过"
```

**策略 3：错误分类沉淀**
```
错误分类：
1. 配置类错误（CORS、环境变量）
2. 网络类错误（超时、连接失败）
3. 业务逻辑错误（验证失败、权限不足）
4. 系统错误（数据库、第三方服务）

每类错误对应：
- 诊断脚本
- 修复模板
- 预防措施
```

**策略 4：渐进式发布**
```
发布流程：
1. 本地环境测试 ✓
2. 测试环境验证 ✓
3. 预发布环境 smoke test ✓
4. 生产环境灰度发布（10% → 50% → 100%）
5. 监控关键指标 24 小时
```

**策略 5：持续监控**
```javascript
// 关键指标监控
const metrics = {
  errorRate: calculateErrorRate(),      // 失误率
  responseTime: getAverageResponseTime(), // 响应时间
  successRate: calculateSuccessRate(),   // 成功率
  userSatisfaction: getCSAT()           // 用户满意度
};

// 自动告警
if (metrics.errorRate > 0.1) {
  sendAlert('失误率超过 10%');
}
```

### 4. 成功模式打包

#### 4.1 识别成功模式
```
成功模式特征：
✓ 解决了实际问题
✓ 可复用于其他场景
✓ 有清晰的文档
✓ 有测试覆盖
✓ 性能可接受
```

#### 4.2 打包成 Skill
```markdown
# Skill 模板

## 名称
[功能名称]

## 描述
[一句话说明解决什么问题]

## 触发场景
[什么时候使用这个 skill]

## 核心代码
[关键实现]

## 使用示例
[如何调用]

## 注意事项
[使用限制和注意事项]
```

#### 4.3 实际案例：CORS 诊断 Skill
```bash
#!/bin/bash
# cors-diagnosis.sh

DOMAIN=$1
ENDPOINT=$2

echo "🔍 诊断 CORS 配置..."

# 测试预检请求
RESPONSE=$(curl -sI -X OPTIONS "$ENDPOINT" \
  -H "Origin: $DOMAIN" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type")

# 检查关键头
ALLOW_ORIGIN=$(echo "$RESPONSE" | grep -i "access-control-allow-origin")
ALLOW_CREDS=$(echo "$RESPONSE" | grep -i "access-control-allow-credentials")

echo "Allow-Origin: $ALLOW_ORIGIN"
echo "Allow-Credentials: $ALLOW_CREDS"

# 检测冲突
if echo "$ALLOW_ORIGIN" | grep -q "\*" && \
   echo "$ALLOW_CREDS" | grep -q "true"; then
  echo "❌ 发现 CORS 配置冲突！"
  echo "修复建议：将 origin 从 * 改为具体域名"
  exit 1
fi

echo "✓ CORS 配置正常"
```

## 输出格式

### 代码审查报告
```markdown
# 代码审查报告

## 项目概览
- 项目名称：[name]
- 技术栈：[stack]
- 审查日期：[date]

## 发现的问题

### 严重问题（必须修复）
1. [问题描述]
   - 影响：[影响范围]
   - 修复方案：[具体步骤]
   - 预计时间：[工作量]

### 中等问题（建议修复）
1. [问题描述]
   - 影响：[影响范围]
   - 修复方案：[具体步骤]

### 轻微问题（可选优化）
1. [问题描述]
   - 优化方案：[具体步骤]

## 失误率分析
| 功能模块 | 当前失误率 | 目标失误率 | 改进措施 |
|---------|-----------|-----------|---------|
| [模块1] | [x%] | [y%] | [措施] |

## 成功模式
1. [模式名称]
   - 应用场景：[场景]
   - 复用价值：[高/中/低]
   - 是否打包：[是/否]

## 下一步行动
- [ ] [行动1] - [负责人] - [截止日期]
- [ ] [行动2] - [负责人] - [截止日期]
```

## 工具推荐

### 静态分析
- ESLint（JavaScript/TypeScript）
- Pylint（Python）
- SonarQube（多语言）

### 安全扫描
- npm audit（Node.js）
- Safety（Python）
- OWASP ZAP（Web 应用）

### 性能分析
- Lighthouse（前端）
- Artillery（API 负载测试）
- Prometheus + Grafana（监控）

## 最佳实践

1. **批判要建设性**：指出问题的同时给出解决方案
2. **优先级清晰**：严重 > 中等 > 轻微
3. **量化指标**：用数据说话（失误率、响应时间）
4. **持续改进**：每次审查后更新检查清单
5. **知识沉淀**：成功模式及时打包分享
