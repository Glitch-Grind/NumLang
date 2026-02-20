@echo off
REM NumLang v1.2 Standalone IDE Launcher
REM This script starts the NumLang IDE and opens it in your default browser

setlocal enabledelayedexpansion

cd /d "%~dp0"

echo.
echo ============================================================
echo             NumLang v1.2 IDE
echo ============================================================
echo.
echo Starting server on http://localhost:5000
echo Opening IDE in your default browser...
echo.
echo Press Ctrl+C to stop the server
echo ============================================================
echo.

REM Check if Python is available
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.x from python.org
    pause
    exit /b 1
)

REM Check if required packages are installed
python -c "import flask; import flask_cors" >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Installing required packages...
    python -m pip install flask flask-cors -q
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Start the IDE
python launcher.py

endlocal
