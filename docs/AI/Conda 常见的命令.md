# Conda 常见的命令

### 环境管理

1. **创建新环境**  
   创建一个名为 `myenv` 的环境，并指定 Python 版本为 3.9：
   
   ```bash
   conda create --name myenv python=3.9
   ```
   
   如果需要同时安装其他包，可以添加包名，例如：
   
   ```bash
   conda create --name myenv python=3.9 numpy pandas。
   ```

2. **激活环境**  
   激活名为 `myenv` 的环境：
   
   ```bash
   conda activate myenv
   ```

3. **退出环境**  
   退出当前激活的环境：
   
   ```bash
   conda deactivate
   ```

4. **删除环境**  
   删除名为 `myenv` 的环境及其所有包：
   
   ```bash
   conda remove --name myenv --all
   ```

5. **列出所有环境**  
   显示所有已创建的 Conda 环境：
   
   ```bash
   conda env list
   ```

6. **克隆环境**  
   克隆一个现有环境，例如将 `myenv` 克隆为 `myenv_clone`：
   
   ```bash
   conda create --name myenv_clone --clone myenv
   ```

### 包管理

1. **安装包**  
   在当前环境中安装 `numpy` 包：
   
   ```bash
   conda install numpy
   ```
   
   或指定版本安装：
   
   ```bash
   conda install numpy=1.21.0
   ```

2. **更新包**  
   更新当前环境中的 `numpy` 包：
   
   ```bash
   conda update numpy
   ```
   
   更新所有包：
   
   ```bash
   conda update --all
   ```

3. **卸载包**  
   卸载当前环境中的 `numpy` 包：
   
   ```bash
   conda remove numpy
   ```

4. **列出已安装的包**  
   显示当前环境中安装的所有包及其版本：
   
   ```bash
   conda list
   ```

5. **搜索包**  
   搜索可用的包及其版本：
   
   ```bash
   conda search numpy
   ```
   
   或使用模糊搜索：
   
   ```bash
   conda search py
   ```

### 其他常用命令

1. **导出环境配置**  
   将当前环境的配置导出为 `environment.yml` 文件：
   
   ```bash
   conda env export > environment.yml
   ```

2. **从配置文件创建环境**  
   根据 `environment.yml` 文件创建环境：
   
   ```bash
   conda env create -f environment.yml
   ```

3. **清理缓存**  
   清理 Conda 的缓存文件，释放磁盘空间：
   
   ```bash
   conda clean --all
   ```

4. **更新 Conda**  
   更新 Conda 工具本身：
   
   ```bash
   conda update conda
   ```

5. **切换国内镜像源**  
   使用国内镜像源（如清华源）加速安装：
   
   ```bash
   conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
   conda config --set show_channel_urls yes
   ```

这些命令可以帮助你高效地管理 Conda 环境和包。
