# NumLang

A lightweight programming language designed for mathematical computations, data manipulation, and algorithmic thinking with a **web-based IDE** featuring syntax highlighting, control flow, and live execution.

**File Extension:** `.numlang`

---

## 📋 About

NumLang is a feature-rich programming language for mathematical expressions, string/list manipulation, file I/O, and calculations. It combines the simplicity of a calculator with the power of a full programming language. This repository contains a fully-functional web-based IDE built with HTML5 Canvas and Python, a command-line REPL interpreter with interactive debugging, and comprehensive examples.

---

## 🎯 Language Features

### Variables
Declare variables using the `let` keyword:
```numlang
let x = 10
let y = 5.5
let result = x + y
let name = "NumLang"
```

### Output
Print values using the `print` keyword:
```numlang
print 42
print x + y
print sqrt(16)
print "Hello, World!"
```

### Lists & Array Operations
Create and manipulate lists:
```numlang
let list = [1, 2, 3, 4, 5]
print len(list)                # Output: 5
let item = pop(list)           # Remove last item
append(list, 10)               # Add to list
```

### Strings & String Manipulation
Work with text:
```numlang
let greeting = "Hello"
print upper(greeting)          # Output: HELLO
print lower(greeting)          # Output: hello
let words = split("a,b,c", ",")  # Convert to list
let message = join(words, " ")    # Convert to string
```

### String Concatenation
Concatenate strings with the `.` operator:
```numlang
let name = "World"
let message = "Hello, " . name . "!"
print message                  # Output: Hello, World!
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
- `len(x)` - Length of string or list

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

**String Operations:**
- `upper(s)` - Convert to uppercase
- `lower(s)` - Convert to lowercase
- `split(s, sep)` - Split string into list
- `join(list, sep)` - Join list into string

**List Operations:**
- `append(list, item)` - Add item to list
- `pop(list, index)` - Remove and return item from list
- `len(list)` - Get list length

**File I/O:**
- `read_file(filename)` - Read file contents
- `write_file(filename, content)` - Write to file
- `append_file(filename, content)` - Append to file

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

### File I/O
Read and write files:
```numlang
# Read file
let content = read_file("data.txt")
print content

# Write to file
write_file("output.txt", "Hello, File!")

# Append to file
append_file("log.txt", "New log entry")
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

### Working with Lists
```numlang
let numbers = [1, 2, 3, 4, 5]
for i = 1 to len(numbers) do
    print numbers[i - 1]
end
```

### String Processing
```numlang
let text = "Hello, NumLang!"
print upper(text)
print lower(text)

let sentence = "one,two,three"
let words = split(sentence, ",")
let result = join(words, "-")
print result
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

### File Operations
```numlang
# Write data to file
write_file("numbers.txt", "1,2,3,4,5")

# Read and process
let data = read_file("numbers.txt")
print data

# Append more data
append_file("numbers.txt", "\n6,7,8,9,10")
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

### CLI Mode & REPL

You can run NumLang interactively from the command line:
```bash
python numlang.py
```

Interactive commands:
- `exit` - Quit the interpreter
- `clear` - Clear all variables and functions
- `vars` / `debug` - Show all defined variables and functions
- `debug on/off` - Toggle debug mode
- `help` - Show language reference

Example session:
```
>>> let x = 10
>>> let y = 20
>>> print x + y
30
>>> function square(n) = n * n
>>> print square(7)
49
>>> vars
[Variables]
  x = 10
  y = 20
[Functions]
  square
```

---

## ✨ Current Features (v1.2)

### Core Language
- ✅ **Variables** - `let` keyword for variable assignment
- ✅ **Functions** - User-defined functions with parameters
- ✅ **Control Flow** - `if/then/end` conditionals and `for/do/end` loops
- ✅ **Comments** - `#` for single-line comments

### Data Types
- ✅ **Numbers** - Integers and floating-point numbers
- ✅ **Strings** - Text manipulation with concatenation using `.`
- ✅ **Lists** - Dynamic arrays with append/pop operations

### Operations & Functions
- ✅ **Math Operators** - `+`, `-`, `*`, `/`, `^` (power), `%` (modulo), `//` (integer division)
- ✅ **Comparison** - `>`, `<`, `>=`, `<=`, `==`, `!=`
- ✅ **String Concatenation** - `.` operator for joining strings
- ✅ **20+ Math Functions** - sqrt, sin, cos, tan, log, exp, pow, abs, floor, ceil, round, deg, rad, etc.
- ✅ **String Functions** - upper, lower, split, join, len
- ✅ **List Functions** - append, pop, len
- ✅ **File I/O** - read_file, write_file, append_file
- ✅ **Math Constants** - pi, e, tau, inf, nan

### IDE Features
- ✅ **Canvas-based Editor** - Custom-built with smooth text rendering
- ✅ **Syntax Highlighting** - Color-coded keywords, numbers, functions, operators, constants
- ✅ **Live Execution** - Run code instantly from the browser
- ✅ **Error Identification** - Visual indication of lines with errors
- ✅ **File Operations** - Open/Save `.numlang` files (Ctrl+O / Ctrl+S)
- ✅ **Auto-indentation** - Smart indentation for control structures
- ✅ **Line Numbers** - Easy navigation and error tracking
- ✅ **Modern Dark UI** - Responsive design, visual feedback

### Debugging & REPL
- ✅ **Interactive REPL** - Execute code line-by-line with state persistence
- ✅ **Debug Mode** - Toggle debugging with `debug on/off`
- ✅ **Variable Inspection** - `vars` command to inspect all variables/functions
- ✅ **Error Stack Traces** - Detailed error information in debug mode
- ✅ **Command Help** - `help` command in REPL for language reference

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

## 📖 Version History

**v1.2** - Major expansion with arrays, strings, file I/O, debugging, and REPL
- Added list/array support with operations
- Added string manipulation functions
- Added file I/O operations
- Implemented interactive REPL with debugging
- Improved error messages with debugging info
- Enhanced with help command and variable inspection

**v1.1** - Control flow and functions
- Added if/then/end conditionals
- Added for/do/end loops
- Added user-defined functions
- Expanded math library

**v1.0** - Initial release
- Basic variables and arithmetic
- Core mathematical functions and constants

---

## 📄 License

This project was created as a learning exercise.
