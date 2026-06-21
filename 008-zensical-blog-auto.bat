@echo off
chcp 1252 >nul
setlocal enabledelayedexpansion

set PROJECT_PATH=blog
set PORT=80

echo ^>^>^> Zensical Blog Project Init Starting...
echo.

:: Step 0: Check and install zensical
echo [0/4] Checking zensical installation...

zensical --version >nul 2>nul
if errorlevel 1 (
    echo     zensical not found. Installing now...

    pip --version >nul 2>nul
    if errorlevel 1 (
        echo     ERROR: pip not found. Please install Python first.
        exit /b 1
    )

    echo     Installing zensical via pip...
    pip install zensical
    if errorlevel 1 (
        echo     ERROR: Failed to install zensical
        exit /b 1
    )

    echo     zensical installed successfully!
) else (
    for /f "tokens=*" %%a in ('zensical --version 2^>nul') do (
        echo     Found zensical %%a
    )
)

:: Step 1: Create blog folder and init
echo.
echo [1/4] Creating %PROJECT_PATH% folder and initializing...

if not exist "%PROJECT_PATH%" (
    mkdir "%PROJECT_PATH%"
    echo     Created folder: %PROJECT_PATH%
) else (
    echo     Folder exists: %PROJECT_PATH%
)

cd /d "%PROJECT_PATH%"

if exist "zensical.toml" (
    echo     zensical.toml found, skipping init
) else (
    echo     Initializing project...
    zensical new .
    if errorlevel 1 (
        echo     ERROR: Init failed
        exit /b 1
    )
    echo     Init completed
)

:: Step 2: Start dev server
echo.
echo [2/4] Starting dev server http://127.0.0.1:%PORT% ...
echo     Tip: Close server window to continue build...
cmd /k zensical serve --open --dev-addr 127.0.0.1:%PORT%

echo.
echo     Server closed, continuing...

:: Step 3: Build
echo.
echo [3/4] Building site...
zensical build
if errorlevel 1 (
    echo     ERROR: Build failed
    exit /b 1
)

echo.
echo     Build completed! Project location: %CD%
echo.
echo     Project structure:
dir /b /a

if exist "site" (
    echo.
    echo     Build output (site/):
    dir /b site)

echo.
echo ^>^>^> All done!
pause
