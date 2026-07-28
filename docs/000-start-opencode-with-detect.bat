@echo off
chcp 65001 >nul 2>&1

echo ============================================
echo   OpenCode Startup Script
echo ============================================
echo.

cd /d "%~dp0"

echo Checking opencode-ai...
where opencode >nul 2>&1
if errorlevel 1 (
    echo Installing opencode-ai...
    call npm i -g opencode-ai
    if errorlevel 1 (
        echo [ERROR] Failed to install opencode-ai
        pause
        exit /b 1
    )
    echo [OK] Installation complete
) else (
    echo [OK] opencode-ai is installed
)
echo.

echo Starting OpenCode...
echo.
call opencode

if errorlevel 1 (
    echo.
    echo [ERROR] OpenCode failed to start
    echo.
)

echo.
pause
