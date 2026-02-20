Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  NumLang IDE Launcher" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.x and try again." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Starting NumLang server..." -ForegroundColor Yellow
Write-Host "Server will run on http://localhost:5000" -ForegroundColor Yellow
Write-Host ""

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Start the server in a new window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$scriptDir'; python server.py" -WindowStyle Normal

# Wait a moment for server to start
Start-Sleep -Seconds 3

# Open the editor in default browser
Write-Host "Opening editor in browser..." -ForegroundColor Yellow
$editorPath = Join-Path $scriptDir "editor.html"
if (Test-Path $editorPath) {
    # Use Invoke-Item which reliably opens files with default application
    Invoke-Item $editorPath
} else {
    Write-Host "ERROR: editor.html not found at $editorPath" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Editor opened in browser!" -ForegroundColor Green
Write-Host "  Server is running in a separate window" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Press any key to exit this launcher..." -ForegroundColor Gray
Write-Host "(The server will continue running)" -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
