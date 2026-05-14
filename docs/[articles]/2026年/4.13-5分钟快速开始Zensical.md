# 5 分钟快速开始 Zensical

> 从零到一，快速搭建你的 Zensical 博客

- **Zensical 官方网站**: [https://zensical.org/](https://zensical.org/)
- **Zensical 官方文档**: [https://zensical.org/docs/](https://zensical.org/docs/)

---

## 第一步：环境准备

### 检查 Python 版本

Zensical 需要 Python 3.8 或更高版本。

```bash
python --version

如果版本低于 3.8，请先升级 Python。

!!! tip "推荐版本"  
推荐使用 Python 3.9 或更高版本，以获得最佳性能和兼容性。

### 创建项目目录

```bash
# 创建项目目录
mkdir my-zensical-site
cd my-zensical-site
```

---

## 第二步：安装 Zensical

**强烈推荐使用 Python 虚拟环境** 进行安装，避免依赖冲突。

### 使用 pip 安装（推荐）

#### macOS / Linux

```bash
# 1. 创建虚拟环境
python3 -m venv .venv

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 升级 pip
pip install --upgrade pip

# 4. 安装 Zensical
pip install zensical

# 5. 验证安装
zensical --version
```

#### Windows

```cmd
:: 1. 创建虚拟环境
python3 -m venv .venv

:: 2. 激活虚拟环境
.venv\Scripts\activate

:: 3. 升级 pip
pip install --upgrade pip

:: 4. 安装 Zensical
pip install zensical

:: 5. 验证安装
zensical --version
```

!!! warning "权限问题"  
如果遇到权限错误，可以尝试：  

- macOS/Linux: `pip install --user zensical`  
- 或使用 `sudo pip install zensical`（不推荐）

### 使用 uv 安装（开发者推荐）

```bash
# 初始化项目
uv init

# 添加 Zensical
uv add zensical

# 验证安装
uv run zensical --version
```

---

## 第三步：创建项目

```bash
# 创建新项目（. 表示当前目录）
zensical new .
```

### 检查项目结构

标准的项目结构如下：

```text
.
├── .github/          # GitHub Actions 工作流
│   └── workflows/
│       └── ci.yml
├── docs/             # 文档源文件
│   ├── index.md      # 网站首页
│   └── markdown.md   # Markdown 示例
└── zensical.toml     # 配置文件
```

---

## 第四步：配置项目

打开 `zensical.toml` 文件进行配置。

### 基础配置

`site_name` 是唯一必需的设置：

```toml
[project]
site_name = "我的博客"
```

### 推荐配置

```toml
[project]
site_name = "我的博客"
site_url = "https://example.com"
site_description = "我的 Zensical 博客"
site_author = "你的名字"
docs_dir = "docs"
site_dir = "site"

# 主题配置（必须在父表配置之后）
[project.theme]
variant = "modern"
language = "zh"
```

!!! warning "配置顺序很重要"  
在 TOML 配置文件中，必须先配置所有 `[project]` 的键值对，然后才能声明子表（如 `[project.theme]`）。

---

## 第五步：启动开发服务器

```bash
# 启动开发服务器
zensical serve
```

访问 `http://localhost:8000` 即可预览。

!!! tip "实时预览"  

- 修改 `docs/` 下的文件，网站会自动刷新。  
- 修改 `zensical.toml` 后，需要手动刷新浏览器。  
- 按 `Ctrl+C` 停止服务器。

### 端口占用处理

如果 8000 端口被占用：

```bash
zensical serve --port 8001
```

---

## 第六步：创建第一篇文章（可选）

### 配置博客插件

在 `zensical.toml` 中添加：

```toml
[project.plugins.blog]
post_date_format = "full"
post_readtime = true
post_readtime_words_per_minute = 265
draft = true
```

### 创建目录与文件

1. 创建目录：`mkdir -p docs/blog/posts`
2. 创建博客首页：`touch docs/blog/index.md` (内容为 `# 博客`)
3. 创建文章：`docs/blog/posts/2025-01-22-hello-world.md`

文章头部（Front Matter）示例：

```markdown
---
title: Hello World
date: 2025-01-22
authors:
  - name: 你的名字
categories:
  - 开始
---
# Hello World
这是我的第一篇 Zensical 博客文章！
```

---

## 第七步：构建网站

构建静态文件：

```bash
# 构建网站
zensical build

# 推荐：清理构建（清除旧文件）
zensical build --clean
```

构建完成后，文件会生成在 `site/` 目录中，你可以将其部署到 GitHub Pages 或 CDN。

---

## 完成！🎉

恭喜！你已经成功创建了一个 Zensical 博客。

### 常用命令速查

| 命令                | 说明      |
| ----------------- | ------- |
| `zensical serve`  | 启动开发服务器 |
| `zensical build`  | 构建静态网站  |
| `zensical --help` | 查看帮助    |

### 修改说明：

1. **代码块分隔符**：我使用了三个反引号 ``` 加上语言标识（如 `bash`, `toml`）来包裹代码，这是最标准的 Markdown 代码块写法。
2. **去除了多余的空行**：在某些静态站点生成器中，代码块前后的多余空行可能会导致渲染异常，我已进行了优化。
3. **Windows 命令处理**：将 Windows 命令单独列出并使用 `cmd` 语言标识，避免与 Linux 命令混淆。
4. **简化结构**：为了确保兼容性，去除了部分过于复杂的嵌套提示框，保留了核心的 `!!! tip` 和 `!!! warning`。

你可以直接复制上面的内容保存为 `.md` 文件，它应该能被正确解析。
