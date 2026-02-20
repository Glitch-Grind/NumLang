# NumLang Distribution & Standalone Setup

## Easy Methods to Run NumLang

### Method 1: Run the Batch File (Windows)
**Easiest way - No Python knowledge required**

1. Download or clone the repository
2. Go to the NumLang folder
3. **Double-click `run-ide.bat`**
4. The IDE will automatically open in your browser

The batch file:
- Checks if Python is installed
- Installs required packages if needed
- Starts the server automatically
- Opens the IDE in your default browser

### Method 2: Use the PowerShell Script
```powershell
.\start-editor.ps1
```

### Method 3: Run from Command Line
```bash
python launcher.py
```

The launcher will:
- Start the Flask server on `http://localhost:5000`
- Open the IDE in your default browser
- Keep running until you press Ctrl+C

### Method 4: Run the REPL Interpreter
```bash
python numlang.py
```

This opens an interactive command-line interpreter where you can:
- Type NumLang code line-by-line
- Use `vars` to inspect variables
- Use `debug on/off` for debugging
- Use `help` for language reference
- Type `exit` to quit

## Building a Standalone Executable

If you want to create a standalone `.exe` file that doesn't require Python:

### Prerequisites
- Python 3.x installed
- PyInstaller: `pip install PyInstaller`

### Build Command
```bash
python -m PyInstaller launcher.py --onefile --add-data "editor.html;." --add-data "fonts;fonts" --hidden-import=flask --hidden-import=flask_cors --name=NumLang
```

The executable will be created in the `dist/` folder as `NumLang.exe`.

**Note:** Building requires a stable Python environment (3.10 or 3.11 recommended). Python 3.15 alpha has compatibility issues.

## Requirements

- Python 3.8+
- Flask (`pip install flask flask-cors`)

The batch file `run-ide.bat` will automatically install Flask if needed.

## Supported Platforms

- Windows (batch file `run-ide.bat`)
- Windows/Mac/Linux (command line: `python launcher.py`)
- Windows/Mac/Linux (REPL: `python numlang.py`)

## Troubleshooting

**"Python not found"**
- Install Python from https://python.org
- Make sure to check "Add Python to PATH" during installation

**"ModuleNotFoundError: No module named 'flask'"**
- Run: `python -m pip install flask flask-cors`
- Or use `run-ide.bat` which handles this automatically

**Port 5000 already in use**
- Close other applications using port 5000
- Or edit `launcher.py` to use a different port

---

**Latest Version:** v1.2
**Author:** Your Name
