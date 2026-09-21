## DeepSeek Harness 的安装步骤

### 🔧 第一步：安装 Node.js（前置条件）

DeepSeek Harness 是用 Node.js 写的，所以第一步必须安装它。

- **版本要求**：**Node.js ≥ 22.19**，官方推荐使用 **24 LTS** 版本。注意，Node 18 或 20 会报错，但错误信息可能不会直接提示版本太低，容易误判。
- **下载安装**：去 [nodejs.org](https://nodejs.org) 下载最新 LTS 版。安装时**务必勾选“添加到 PATH”**，装完后重新打开一个终端窗口。
- **验证安装**：在终端输入以下命令检查版本：
  
  ```bash
  node --version
  npm --version
  ```
  
  只要 `node --version` 显示 v22.19 或更高即可。

### 🚀 第二步：选择安装方式启动 Harness

Node.js 就绪后，有两种方式运行 DeepSeek Harness。**推荐初次尝鲜用方式 A**。

#### 方式 A：npx 一行启动（推荐尝鲜）

这是最省事的方法，官方也只给了这一条安装指令。在终端直接运行：

```bash
npx @deepseek-ai/dsh web
```

首次运行会提示是否下载包，输入 `y` 回车即可。下载完成后，终端会打印出地址 `http://127.0.0.1:3080`，浏览器打开就能进入界面。

> **小提示**：国内用户可以先配置 npm 镜像源加速下载：
> 
> ```bash
> npm config set registry https://registry.npmmirror.com
> ```

**这种方式的特点**：不长期占用磁盘、每次运行都是最新版；但关掉终端服务就停，不适合开机自启。

#### 方式 B：源码安装（适合开发或长期使用）

如果你要开发插件或跟进 main 分支，用源码方式：

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

这种方式需要额外安装 **pnpm 11 或更高版本**，可通过 Corepack 启用。

如果想全局安装，也可以直接：

```bash
npm install -g @deepseek-ai/dsh
dsh web
```

全局安装的优点是命令短、可配合开机自启；缺点是版本固定，更新需手动执行 `npm update -g @deepseek-ai/dsh`。

### ⚙️ 第三步：首次配置与使用

浏览器打开 `http://127.0.0.1:3080` 后，首次使用需要完成两步配置：

1. **填入 API Key**：去 [platform.deepseek.com](https://platform.deepseek.com) 注册并创建 API Key，粘贴到 Harness 的设置中。Key 会保存在本地 `~/.dsh/.credentials.yaml` 文件里。
2. **选择工作区**：在主界面选择你的项目目录，然后就可以开始让 DeepSeek 帮你读文件、改代码、执行命令了。

### 📋 完整流程速览

```
安装 Node.js (≥22.19) → 配置 NPM 镜像(可选) → npx @deepseek-ai/dsh web → 
浏览器打开 127.0.0.1:3080 → 填入 API Key → 选择工作区 → 开始使用
```

整个过程顺利的话，**10 分钟左右**就能跑通第一个任务。如果遇到 `npx` 找不到命令，通常是因为 Node.js 安装时没勾选“添加到 PATH”，重装并勾选后重开终端即可解决。
