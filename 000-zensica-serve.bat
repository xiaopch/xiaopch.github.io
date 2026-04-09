::python -m venv .venv
::cmd /k .venv\Scripts\activate
::zensical new .

@echo off
setlocal enabledelayedexpansion

:: 设置端口范围
set /a min=10000
set /a max=60000

:: 生成随机端口
set /a range=max-min+1
set /a port=%random% %% range + min

:: 启动服务
echo 使用随机端口: %port%
cmd /k zensical serve --open -a 127.0.0.1:%port%
zensical serve --open -a 127.0.0.1:0
zensical build