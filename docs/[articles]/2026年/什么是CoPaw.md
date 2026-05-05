## 什么是 CoPaw

CoPaw（Co Personal Agent Workstation）是一款**可本地、可云端部署**的个人 AI 助理。

- **核心定位**：它不仅是一个聊天机器人，更是一个可扩展的智能工作站。你可以将其视为你的“数字伙伴”，通过接入钉钉、飞书、微信等渠道，帮你处理日程、文件、信息检索等任务。
- **开源协议**：Apache 2.0（支持免费商用、源码可审计）。
- **最新动态**：已于 2026 年 3 月 30 日发布 **v1.0.0** 正式版，标志着核心功能的稳定。

### 🚀 核心亮点

1. **全链路隐私保护**：支持纯本地部署（数据留在本地机器）或云端部署，无第三方托管。
2. **多模型支持**：既支持云端大模型（如 Qwen、OpenAI），也原生支持本地模型（Ollama、llama.cpp、LM Studio、MLX）。
3. **多渠道接入**：支持钉钉、飞书、微信、QQ、Discord、Telegram 等主流聊天软件。
4. **无限扩展（Skills）**：通过 Skills 机制，你可以编写或安装插件（如新闻摘要、文件搜索、代码执行），让 AI 能力无限延伸。
5. **多智能体协作**：支持创建多个独立 Agent，它们可以相互协作完成复杂任务。

---

### 💻 安装与启动指南

CoPaw 提供了多种安装方式，以适应不同的技术背景。

#### 1. 脚本一键安装（推荐，无需配置 Python 环境）

适用于希望快速体验、不想手动安装 Python 的用户。

- **macOS / Linux**：
  
  ```
  curl -fsSL https://copaw.agentscope.io/install.sh | bash
  ```
  
  *若需支持 Ollama*：
  
  ```
  curl -fsSL https://copaw.agentscope.io/install.sh | bash -s -- --extras ollama
  ```

- **Windows (PowerShell)**：
  
  ```
  irm https://copaw.agentscope.io/install.ps1 | iex
  ```

#### 2. Pip 安装（需自行配置 Python >=3.10）

适用于熟悉 Python 环境的开发者。

    pip install copaw

    copaw init --defaults

    copaw app


#### 3. Docker 安装

适用于已有 Docker 环境的用户。

    docker pull agentscope/copaw:latest

    docker run -p 127.0.0.1:8088:8088 \
      -v copaw-data:/app/working \
      -v copaw-secrets:/app/working.secret \
      agentscope/copaw:latest


*访问地址*：启动后，在浏览器打开 `http://127.0.0.1:8088/` 即可进入控制台。

---

### 📊 本地模型配置速查表

| 后端类型          | 适用场景                 | 安装/配置要点                              
| ------------- | -------------------- | --------------------------------------------- |
| **Ollama**    | 跨平台，生态丰富             | 需提前安装 Ollama 应用；安装脚本时添加 `--extras ollama` 参数。 |
| **llama.cpp** | 跨平台 (Mac/Win/Linux)  | 无需额外安装；在 Web UI 中点击 "Download Llama.cpp" 即可。  |
| **LM Studio** | 跨平台 (需开启 Web Server) | 需提前安装并启动 LM Studio 应用。                        |
| **MLX**       | Apple Silicon (M芯片)  | 需通过 pip 安装额外依赖：`pip install "copaw[mlx]"`。    |

> **💡 提示**：使用本地模型（如 Ollama、llama.cpp）**不需要**配置云端 API Key。

---

### 📅 未来规划与 Roadmap

根据官方路线图，CoPaw 接下来的重点发展方向包括：

- **多模态交互**：支持语音/视频通话和实时交互。
- **大小模型协作**：利用云端大模型处理复杂规划，本地小模型处理隐私数据，兼顾安全与性能。
- **云原生架构**：结合 AgentScope Runtime，利用云端算力与存储。
- **技能中心 (Skills Hub)**：丰富社区生态，方便用户发现和使用高质量插件。

### 🔗 参考资料

- **GitHub 仓库**：https://github.com/agentscope-ai/CoPaw
- **官方文档**：[https://copaw.agentscope.io/](https://copaw.agentscope.io/)
- **安装脚本源码**：https://copaw.agentscope.io/install.sh
