@echo off
echo ========================================
echo   NumLang IDE Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.x and try again.
    pause
    exit /b 1
)

echo Starting NumLang server...
echo Server will run on http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the server in a new window
start "NumLang Server" cmd /k "cd /d %~dp0 && python server.py"

REM Wait a moment for server to start
timeout /t 3 /nobreak >nul

REM Open the editor in default browser
echo Opening editor in browser...
cd /d %~dp0
if exist "%~dp0editor.html" (
    REM Use rundll32 to open with default browser (most reliable method)
    rundll32 url.dll,FileProtocolHandler "%~dp0editor.html"
) else (
    echo ERROR: editor.html not found!
    echo Current directory: %~dp0
    dir /b *.html
    pause
)

echo.
echo ========================================
echo   Editor opened in browser!
echo   Server is running in a separate window
echo ========================================
echo.
pause
