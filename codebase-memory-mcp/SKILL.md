# Codebase Memory MCP

高性能代码智能 MCP 服务器，将代码库索引到持久化知识图谱中。

## 功能特性

- **极速索引**：Linux 内核（28M 行，75K 文件）仅需 3 分钟
- **158 种语言**：支持 Python、TypeScript、Go、Rust、Java 等主流语言
- **14 个 MCP 工具**：搜索、追踪、架构分析、影响分析等
- **零依赖**：单个静态二进制文件，无需 Docker 或运行时依赖
- **11 个代理支持**：Claude Code、Codex CLI、Gemini CLI、Zed 等

## 安装

### 一键安装（推荐）

```bash
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash
```

带图形可视化 UI：
```bash
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --ui
```

### Windows 安装

```powershell
Invoke-WebRequest -Uri https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.ps1 -OutFile install.ps1
.\install.ps1
```

## 快速开始

1. 安装后重启你的编码代理
2. 说 "Index this project" 开始索引
3. 使用自然语言查询代码库

## 核心工具

### 索引工具
- `index_repository` - 索引代码库到知识图谱
- `list_projects` - 列出所有已索引项目
- `delete_project` - 删除项目及其图数据
- `index_status` - 检查项目索引状态

### 查询工具
- `search_graph` - 结构化搜索（标签、名称模式、文件模式）
- `trace_path` - BFS 遍历调用路径
- `detect_changes` - 映射 git diff 到受影响的符号
- `query_graph` - 执行 Cypher 风格的图查询
- `get_architecture` - 获取代码库架构概览
- `search_code` - 在索引文件中搜索代码
- `manage_adr` - 管理架构决策记录

## 使用示例

### CLI 模式

```bash
# 索引项目
codebase-memory-mcp cli index_repository '{"repo_path": "/path/to/repo"}'

# 搜索函数
codebase-memory-mcp cli search_graph '{"name_pattern": ".*Handler.*", "label": "Function"}'

# 追踪调用路径
codebase-memory-mcp cli trace_path '{"function_name": "Search", "direction": "both"}'

# Cypher 查询
codebase-memory-mcp cli query_graph '{"query": "MATCH (f:Function) RETURN f.name LIMIT 5"}'
```

### 图形可视化

```bash
codebase-memory-mcp --ui=true --port=9749
```

然后在浏览器打开 `http://localhost:9749`

## 配置

```bash
# 显示所有设置
codebase-memory-mcp config list

# 启用自动索引
codebase-memory-mcp config set auto_index true

# 设置自动索引文件限制
codebase-memory-mcp config set auto_index_limit 50000

# 重置配置
codebase-memory-mcp config reset auto_index
```

## 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `CBM_CACHE_DIR` | `~/.cache/codebase-memory-mcp` | 数据库存储目录 |
| `CBM_DIAGNOSTICS` | `false` | 启用诊断输出 |
| `CBM_LOG_LEVEL` | `info` | 日志级别（debug/info/warn/error/none） |

## 性能指标

- **Linux 内核完整索引**：3 分钟（28M 行，75K 文件）
- **Django 完整索引**：~6 秒（49K 节点，196K 边）
- **Cypher 查询**：<1ms
- **名称搜索**：<10ms
- **死代码检测**：~150ms

## 支持的语言

**优秀（>= 90%）**：Lua、Kotlin、C++、Perl、Objective-C、Groovy、C、Bash、Zig、Swift、CSS、YAML、TOML、HTML、SCSS、HCL、Dockerfile

**良好（75-89%）**：Python、TypeScript、TSX、Go、Rust、Java、R、Dart、JavaScript、Erlang、Elixir、Scala、Ruby、PHP、C#、SQL

**功能（< 75%）**：OCaml、Haskell

## 卸载

```bash
codebase-memory-mcp uninstall
```

## 相关链接

- GitHub: https://github.com/DeusData/codebase-memory-mcp
- 论文: https://arxiv.org/abs/2603.27277
- 文档: 查看项目 docs 目录
