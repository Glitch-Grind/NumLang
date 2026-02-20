# NumLang

A lightweight programming language designed for mathematical computations with a **web-based IDE** featuring syntax highlighting, control flow, and live execution.

**File Extension:** `.numlang`

---

## 📋 About

NumLang is a minimal but feature-rich programming language for mathematical expressions, calculations, and algorithmic thinking. It includes variables, conditionals, loops, user-defined functions, and access to a comprehensive set of mathematical functions and constants. This repository contains a fully-functional web-based IDE built with HTML5 Canvas and Python, along with a command-line interpreter.

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

**Basic Math:**
- `sqrt(x)` - Square root
- `abs(x)` - Absolute value
- `floor(x)` - Round down
- `ceil(x)` - Round up
- `round(x)` - Round to nearest
- `exp(x)` - e^x
- `pow(x, y)` - x raised to power y

**Trigonometry:**
- `sin(x)` - Sine (radians)
- `cos(x)` - Cosine (radians)
- `tan(x)` - Tangent (radians)
- `asin(x)` - Arc sine
- `acos(x)` - Arc cosine
- `atan(x)` - Arc tangent
- `deg(x)` - Convert radians to degrees
- `rad(x)` - Convert degrees to radians

**Logarithms:**
- `log(x)` - Natural logarithm (base e)
- `log10(x)` - Base 10 logarithm
- `log2(x)` - Base 2 logarithm

### Mathematical Constants
- `pi` - π (3.14159...)
- `e` - Euler's number (2.71828...)
- `tau` - τ (2π)
- `inf` - Infinity
- `nan` - Not a number

### Operators
- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `/` - Division
- `^` - Exponentiation (power)
- `%` or `mod` - Modulo
- `//` - Integer division
- `()` - Parentheses for grouping

### Comparison Operators
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal
- `<=` - Less than or equal
- `==` - Equal to
- `!=` - Not equal to

### Conditional Statements
Use `if/then/end` for conditional execution:
```numlang
let x = 15
if x > 10 then
    print "x is large"
end

if x == 15 then
    print "x is exactly 15"
end
```

### Loops
Use `for/do/end` for iteration:
```numlang
for i = 1 to 10 do
    print i
end

# Calculate factorial
let fact = 1
for i = 1 to 5 do
    let fact = fact * i
end
print fact
```

### User-Defined Functions
Define your own functions:
```numlang
function square(x) = x * x
function add(x, y) = x + y

print square(5)
print add(3, 4)
```

### Comments
Lines starting with `#` are treated as comments:
```numlang
# This is a comment
let x = 10  # Inline comment
```

---

## 📝 Example Programs

### Calculate Circle Area
```numlang
# Calculate the area of a circle
let radius = 5
let area = pi * radius^2
print area
```

### Trigonometric Functions
```numlang
let angle = pi / 4
print sin(angle)
print cos(angle)
print deg(angle)
```

### Conditional Logic
```numlang
let score = 85
if score >= 90 then
    print "Grade: A"
end
if score >= 80 then
    print "Grade: B"
end
```

### Factorial Calculation
```numlang
let n = 5
let result = 1
for i = 1 to n do
    let result = result * i
end
print result
```

### Custom Functions
```numlang
function distance(x1, y1, x2, y2) = sqrt((x2 - x1)^2 + (y2 - y1)^2)

let d = distance(0, 0, 3, 4)
print d
```

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

## ✨ Current Features

- **Control Flow** - `if/then/end` conditionals and `for/do/end` loops
- **User-Defined Functions** - Create reusable functions with custom parameters
- **Comprehensive Math Library** - 20+ mathematical functions including trigonometry, logarithms, and basic arithmetic
- **Mathematical Constants** - Built-in constants like `pi`, `e`, `tau`, `inf`, and `nan`
- **Canvas-based IDE** - Custom-built editor with smooth text rendering
- **Syntax Highlighting** - Color-coded keywords, numbers, functions, operators, and constants
- **Live Execution** - Run NumLang scripts instantly from the browser
- **Error Reporting** - Detailed error messages with line number references
- **File Operations** - Open and save `.numlang` files (Ctrl+O / Ctrl+S)
- **Auto-indentation** - Automatic indentation for control structures
- **Line Numbers** - Easy navigation and error tracking
- **Modern UI** - Dark theme with responsive design
- **CLI Support** - Run NumLang from the command line interface

---

## 📝 Project Structure

```
NumLang/
├── numlang.py           # Core language interpreter
├── server.py            # Flask backend server
├── editor.html          # Web-based IDE
├── example.numlang      # Example program
├── start-editor.bat     # Quick start script (Windows)
├── start-editor.ps1     # Quick start script (PowerShell)
└── fonts/               # IDE font files
```

---

## 📖 Version Information

**Current Version** - Stable release with full language features and IDE support.

**Initial Release** - Core mathematical language with variables, operators, and functions.

---

## 📄 License

This project was created as a learning exercise.
