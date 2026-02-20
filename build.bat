@echo off
setlocal enabledelayedexpansion

echo.
echo ============================================================
echo NumLang v1.2 Standalone Builder
echo ============================================================
echo.

cd /d "%~dp0"

echo Building executable...
echo.

python -m PyInstaller launcher.py ^
    --onefile ^
    --windowed ^
    --name=NumLang ^
    --add-data "editor.html;." ^
    --add-data "fonts;fonts" ^
    --hidden-import=flask ^
    --hidden-import=flask_cors ^
    --distpath dist ^
    --buildpath build

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================================
    echo Build successful!
    echo Executable: %~dp0dist\NumLang.exe
    echo ============================================================
    echo.
    pause
) else (
    echo.
    echo ============================================================
    echo Build failed! Check the error messages above.
    echo ============================================================
    echo.
    pause
)

endlocal
