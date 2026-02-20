# NumLang 1.0

A simple programming language designed for mathematical computations with a **canvas-based IDE** featuring syntax highlighting and live execution.

---

## 📋 About

NumLang is a minimal programming language focused on mathematical expressions and calculations. This repository contains a fully-functional web-based IDE built with HTML5 Canvas and Python, allowing you to write and execute NumLang scripts directly in your browser.

---

## 🎯 Language Features

### Variables
Declare variables using the `let` keyword:
```numlang
let x = 10
let y = 5.5
let result = x + y
```

### Output
Print values using the `print` keyword:
```numlang
print 42
print x + y
print sqrt(16)
```

### Mathematical Functions
Built-in math functions:
- `sqrt(x)` - Square root
- `sin(x)` - Sine (radians)
- `cos(x)` - Cosine (radians)
- `tan(x)` - Tangent (radians)
- `log(x)` - Natural logarithm

### Mathematical Constants
- `pi` - π (3.14159...)
- `e` - Euler's number (2.71828...)

### Operators
- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `/` - Division
- `^` - Exponentiation (power)
- `()` - Parentheses for grouping

### Comments
Lines starting with `#` are treated as comments:
```numlang
# This is a comment
let x = 10  # Inline comment
```

### Example Program
```numlang
# Calculate the area of a circle
let radius = 5
let area = pi * radius^2
print area

# Use trigonometric functions
let angle = pi / 4
print sin(angle)
print cos(angle)
```

---

## ✨ IDE Features

- **Canvas-based code editor** – Custom-built editor with smooth text rendering
- **Syntax highlighting** – Color-coded keywords, numbers, functions, and operators
- **Live execution** – Run NumLang scripts directly from the browser with a single click
- **Modern UI** – Dark theme with polished interface and visual feedback
- **Output panel** – See results in real-time with success/error indicators
- **Responsive design** – Works on different screen sizes

---

## 🛠️ Tech Stack

- **Frontend**: HTML5 Canvas, JavaScript
- **Backend**: Python (Flask)
- **Language**: Python 3

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Flask (`pip install flask flask-cors`)

### Quick Start (Easiest Way)

**Windows Users:**
- **Double-click** `start-editor.bat` (or `start-editor.ps1` for PowerShell)
- The server will start automatically and the editor will open in your browser!

### Manual Setup

1. **Start the server:**
   ```bash
   python server.py
   ```
   The server will run on `http://localhost:5000`

2. **Open the IDE:**
   - Open `editor.html` in your web browser
   - Or double-click `start-editor.bat` / `start-editor.ps1`

3. **Write and run code:**
   - Type your NumLang code in the editor
   - Click the "▶ Run" button to execute
   - View results in the output panel

### CLI Mode

You can also run NumLang from the command line:
```bash
python numlang.py
```

---

## 📝 Version

**NumLang 1.0** - Initial release with core mathematical features.

---

## 📄 License

This project was created as a learning exercise.