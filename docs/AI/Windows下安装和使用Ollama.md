
## 在 Windows 下使用 Ollama

### 一、安装 Ollama
1. **下载安装程序**：访问 [Ollama Windows Preview 页面](https://ollama.com/download/windows) ，点击下载按钮获取 `OllamaSetup.exe` 安装程序。
2. **运行安装程序**：双击下载的安装文件，点击「Install」开始安装。安装完成后，Ollama 会在系统托盘中显示图标。
3. **退出 Ollama**：安装完成后，右键点击系统托盘中的 Ollama 图标，选择「Quit Ollama」退出后台运行。

### 二、配置 Ollama
1. **更改模型存放路径**（推荐）：
   - 打开「系统环境变量」，新建一个用户变量：
     - 变量名：`OLLAMA_MODELS`
     - 变量值：自定义模型存储路径，例如
     -  `D:\ollama\models`。
   - 如果已启动 Ollama，退出后重新启动，使配置生效。
2. **更改 Ollama API 访问地址和端口**（可选）：
   - 新建用户变量：
     - 变量名：`OLLAMA_HOST`
     - 变量值：自定义端口号，例如 `:8000`。
   - 如果需要在局域网内访问，需在 Windows 防火墙中开放相应端口。
3. **允许浏览器跨域请求**（可选）：
   - 新建用户变量：
     - 变量名：`OLLAMA_ORIGINS`
     - 变量值：`*`。
4. **关闭开机自启动**（可选）：
   - 访问路径 `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`，删除其中的 `Ollama.lnk` 快捷方式文件。

### 三、使用 Ollama
1. **启动 Ollama**：在「开始」菜单中找到并启动 Ollama。
2. **获取并运行 AI 模型**：
   - 打开命令行工具（如 PowerShell 或命令提示符）。
   
   - 使用以下命令加载并运行模型：
     
   - 
     
     ```
     ollama run <model_name>
     ```
     例如：
     
     
     
     ```
     ollama run mistral
     ```
     
     
     常用模型及安装命令如下：
     
     | 模型      | 安装命令              |
     | --------- | --------------------- |
     | Llama 3.3 | `ollama run llama3.3` |
     | Mistral   | `ollama run mistral`  |
     | Qwen2.5   | `ollama run qwen2.5`  |
3. **在命令行中使用模型**：
   - 模型加载完成后，即可在命令行中与 AI 进行交互。
   
   - 例如，使用 Qwen2 模型进行对话：
     
   - 
     
     ```
     ollama run qwen2
     ```
     
   
4. **通过 API 调用 Ollama**：
   - Ollama 提供了兼容 OpenAI 的 Chat Completions API，可以通过 HTTP 请求调用。
   
   - 示例命令：
     
   - 
     
     ```
     curl http://localhost:11434/v1/chat/completions \
         -H "Content-Type: application/json" \
         -d '{
             "model": "phi3:medium-128k",
             "messages": [
                 {
                     "role": "system",
                     "content": "You are a helpful assistant."
                 },
                 {
                     "role": "user",
                     "content": "天空为什么是蓝色的？"
                 }
             ]
         }'
     ```
     
     

### 四、其他注意事项
- **硬件要求**：Ollama 推荐使用 NVIDIA 或 AMD 的 GPU，CPU 运行性能较差。
- **模型存储空间**：下载的模型可能占用大量空间，请确保有足够的磁盘空间。
- **日志查看**：如果遇到问题，可以通过访问 `%LOCALAPPDATA%\Ollama` 查看日志文件。

通过以上步骤，你可以在 Windows 系统上顺利安装、配置并使用 Ollama。

: [Ollama on Windows：本地运行大语言模型的利器 - 系统极客](https://www.xitongjike.com/article/16383.html)

---