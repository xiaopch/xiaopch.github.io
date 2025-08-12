## Windows 系统下使用 Python 的 UV的教程

### 安装 UV

1. **通过 pip 安装**（推荐）：直接使用 Python 自带的 pip 安装，兼容性最佳。
   
   ```
   pip install uv
   ```
   

2. **使用 PowerShell 脚本安装**：打开 PowerShell，执行：
   
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   

3. **使用 winget 安装**：如果已安装 winget，可以使用以下命令：
   
   ```
   winget install --id=astral-sh.uv -e
   ```
   

4. **使用 pipx 安装**：如果已安装 pipx：
   
   ```
   pipx install uv
   ```
   

5. **直接下载安装包**：从 [UV 官方 GitHub 仓库](https://github.com/astral-sh/uv) 下载 `uv-x86_64-pc-windows-msvc.zip`，解压后将解压后的文件夹目录设置环境变量即可生效。


### 验证安装

安装完成后，打开命令提示符或 PowerShell，输入以下命令来验证 UV 是否安装成功：

```
uv --version
```


### 基础用法

1. **创建虚拟环境**：
   
   ```
   uv venv .venv  # 在当前目录下创建一个名为 .venv 的虚拟环境，使用系统默认的 Python 版本
   uv venv -p 3.12  # 指定 Python 版本（需已安装）
   ```
   
   
   激活虚拟环境：
   
   ```
   .venv\Scripts\activate  # Windows
   ```
   

2. **安装依赖包**：语法与 pip 一致，但速度更快。
   
   ```
   uv pip install requests  # 安装 requests 包
   uv pip install Flask==2.2.2  # 安装指定版本的 Flask 包
   uv pip install -r requirements.txt  # 从 requirements.txt 文件安装所有依赖
   ```
   

3. **卸载包**：
   
   ```
   uv pip uninstall requests  # 卸载 requests 包
   uv pip uninstall Flask Werkzeug  # 卸载多个包
   ```
   

4. **列出已安装的包**：
   
   ```
   uv pip list
   ```
   

### 项目管理

1. **初始化项目**：创建一个新项目，会生成默认的文件和目录结构。
   
   ```
   uv init myproject
   cd myproject
   ```
   

2. **添加依赖**：
   
   ```
   uv add requests
   uv add "numpy==1.23.4"
   ```
   

3. **同步项目依赖**：
   
   ```
   uv sync
   ```
   

4. **运行项目**：
   
   ```
   uv run main.py
   ```
   

5. **导出依赖**：
   
   ```
   uv pip freeze > requirements.txt
   ```
   

### Python 版本管理

1. **安装特定版本的 Python**：
   
   ```
   uv python install 3.12
   ```
   
   
   也可以安装多个版本：
   
   ```
   uv python install 3.11 3.12
   ```
   

2. **查看已安装的 Python 版本**：
   
   ```
   uv python list
   ```
   

### 更换国内源

1. **项目配置**：在 `pyproject.toml` 文件中添加：
   
   ```toml
   [[tool.uv.index]]
   url = "https://pypi.tuna.tsinghua.edu.cn/simple"
   default = true
   ```
   
   
   或在 `uv.toml` 文件中添加：
   
   ```toml
   [[index]]
   url = "https://pypi.tuna.tsinghua.edu.cn/simple"
   default = true
   ```
   

2. **环境变量**：在终端中临时设置：
   
   ```
   uv add --default-index https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple fastmcp
   ```
   
   
   或在系统中永久设置：
   
   ```
   vi ~/.bashrc
   export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
   export EXTRA_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
   ```
   

更多高级用法和详细信息可以参考 [UV 官方文档](https://docs.astral.sh/uv/)。
