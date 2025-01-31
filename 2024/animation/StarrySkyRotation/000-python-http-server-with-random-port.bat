@echo off
set /a "port=%RANDOM% %% 64536 + 1024"
start http://localhost:%port%/
cmd /k python -m http.server %port%