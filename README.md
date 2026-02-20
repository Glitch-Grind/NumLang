# NumLang

A **complete** programming language designed for mathematical computations, data manipulation, and scientific problem-solving with a **web-based IDE** featuring syntax highlighting, control flow, and live execution.

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
**Advanced Math:**
- `factorial(x)` - Factorial of x
- `gcd(a, b)` - Greatest common divisor
- `lcm(a, b)` - Least common multiple
- `fabs(x)` - Absolute value (float)
- `sinh(x)`, `cosh(x)`, `tanh(x)` - Hyperbolic functions
- `log1p(x)` - Natural log of (1 + x)

**Trigonometry:**
- `sin(x)`, `cos(x)`, `tan(x)` - Trig functions (radians)
- `asin(x)`, `acos(x)`, `atan(x)` - Arc trig functions
- `atan2(y, x)` - Two-argument arctangent
- `deg(x)` - Convert radians to degrees
- `rad(x)` - Convert degrees to radians

**Logarithms:**
- `log(x)` - Natural logarithm (base e)
- `log10(x)` - Base 10 logarithm
- `log2(x)` - Base 2 logarithm

**Statistics Functions:**
- `sum(list)` - Sum of all elements
- `min(list)` - Minimum value
- `max(list)` - Maximum value
- `mean(list)` - Average (mean) value
- `avg(list)` - Alias for mean
- `median(list)` - Median value
- `stdev(list)` - Standard deviation

**Random Number Generation:**
- `random()` - Random float between 0 and 1
- `randint(a, b)` - Random integer between a and b
- `choice(list)` - Random element from list
- `shuffle(list)` - Shuffle list in-place

**String Operations:**
- `upper(s)` - Convert to uppercase
- `lower(s)` - Convert to lowercase
- `split(s, sep)` - Split string into list
- `join(list, sep)` - Join list into string
- `replace(s, old, new)` - Replace substring
- `strip(s)` - Remove leading/trailing whitespace
- `startswith(s, prefix)` - Check string prefix
- `endswith(s, suffix)` - Check string suffix
- `contains(s, substr)` - Check if substring exists
- `find(s, substr)` - Find index of substring

**List Operations:**
- `append(list, item)` - Add item to list
- `pop(list, index)` - Remove and return item
- `sort(list)` - Sort list in-place
- `reverse(list)` - Reverse list in-place
- `clear(list)` - Clear all items
- `count(list, item)` - Count occurrences
- `index(list, item)` - Find index of item
- `len(list)` - Get list length
- `range(start, end)` - Create list of integers

**Type Conversion:**
- `int(value)` - Convert to integer
- `float(value)` - Convert to float
- `str(value)` - Convert to string
- `bool(value)` - Convert to boolean

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

**For Loops** - Iterate over a range:
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

**While Loops** - Repeat while condition is true:
```numlang
let x = 0
while x < 5 do
    print x
    let x = x + 1
end

# Sum until value reaches threshold
let sum = 0
let i = 1
while sum < 100 do
    let sum = sum + i
    let i = i + 1
end
print sum
```

### Error Handling

**Try/Catch** - Handle errors gracefully:
```numlang
try
    let result = read_file("nonexistent.txt")
    print result
catch
    print "File not found - caught error"
end

# Access error details
try
    let x = 10 / 0
catch
    print error
end
```
````

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

### Quick Start (Recommended - Windows)

**Just double-click `run-ide.bat`**
- The launcher automatically:
  - Installs Python dependencies if needed
  - Starts the server
  - Opens the IDE in your browser
  - No additional setup required!

### Alternative: PowerShell Script

**Windows Users:**
- **Double-click** `start-editor.ps1`
- Or run: `.\start-editor.ps1`

### Manual Setup

1. **Start the server:**
   ```bash
   python launcher.py
   ```
   The server will run on `http://localhost:5000` and open in your browser automatically.

2. **Or open the HTML file directly** (requires manual server start):
   - Open `editor.html` in your web browser
   - Make sure `server.py` is running for full functionality

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

## ✨ Current Features (v1.3 - FINAL)

### Core Language
- ✅ **Variables** - `let` keyword for variable assignment
- ✅ **User-Defined Functions** - Define and call reusable functions with parameters
- ✅ **Full Control Flow** - `if/then/end`, `for/do/end`, `while/do/end` loops
- ✅ **Error Handling** - `try/catch/end` blocks for graceful error handling
- ✅ **Comments** - `#` for single and inline comments

### Data Types & Operations
- ✅ **Numbers** - Integers and floating-point arithmetic
- ✅ **Strings** - Full text manipulation with concatenation (`.` operator)
- ✅ **Lists** - Dynamic arrays with 10+ built-in methods
- ✅ **Math Operators** - `+`, `-`, `*`, `/`, `^`, `%`, `//`
- ✅ **Comparison** - `>`, `<`, `>=`, `<=`, `==`, `!=`

### Mathematical Functions (50+)
- ✅ **Basic Math** - sqrt, abs, floor, ceil, round, factorial, gcd, lcm, exp, pow
- ✅ **Trigonometry** - sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh
- ✅ **Logarithms** - log, log10, log2, log1p
- ✅ **Degree/Radian** - deg(convert to degrees), rad(convert to radians)
- ✅ **20+ Math Constants** - pi, e, tau, inf, nan

### Statistics & Data Analysis
- ✅ **Statistical Functions** - sum, min, max, mean, median, stdev, avg
- ✅ **Random Generation** - random, randint, choice, shuffle
- ✅ **Type Conversion** - int, float, str, bool

### String Operations (10+ methods)
- ✅ **Case Conversion** - upper, lower
- ✅ **Manipulation** - split, join, replace, strip
- ✅ **Search** - find, contains, startswith, endswith
- ✅ **Length** - len

### List Operations (10+ methods)
- ✅ **Modification** - append, pop, sort, reverse, clear
- ✅ **Search** - count, index, choice
- ✅ **Generation** - range
- ✅ **Shuffling** - shuffle

### File I/O
- ✅ **Read/Write** - read_file, write_file, append_file
- ✅ **Error Handling** - Graceful file error handling with try/catch

### IDE Features
- ✅ **Web-Based Editor** - Canvas-based with smooth rendering
- ✅ **Syntax Highlighting** - Keywords, numbers, functions, operators, constants
- ✅ **Live Execution** - Instant code execution from browser
- ✅ **File Management** - Open/Save `.numlang` files (Ctrl+O / Ctrl+S)
- ✅ **Auto-Indentation** - Smart indentation for all block structures
- ✅ **Line Numbers** - Navigation and error tracking
- ✅ **Error Display** - Visual line error indicators
- ✅ **Dark Theme** - Modern UI with responsive design

### Command-Line Features
- ✅ **Interactive REPL** - Full featured interpreter with state persistence
- ✅ **Debug Mode** - `debug on/off` for detailed execution info
- ✅ **Variable Inspection** - `vars` command shows all variables and functions
- ✅ **Error Traces** - Extended error information
- ✅ **Help System** - `help` command for language reference
- ✅ **State Management** - `clear` command to reset environment

---

## 📝 What You Can Build

✅ **Scientific Calculations** - Complex mathematical computations with 50+ functions  
✅ **Data Analysis** - Statistics, aggregations, list processing  
✅ **File Processing** - Read/parse/write data files  
✅ **Algorithms** - Iterative and recursive problem solving  
✅ **Games** - Turn-based logic with random numbers  
✅ **Simulations** - Mathematical models and statistics

---

## 📦 Project Structure

```
NumLang/
├── numlang.py              # Complete language interpreter
├── server.py               # Flask web server
├── launcher.py             # Application launcher
├── editor.html             # Web-based IDE
├── example.numlang         # Comprehensive examples
├── test_advanced.py        # Feature test suite
├── run-ide.bat             # Windows launcher (easiest!)
├── start-editor.bat        # Alternative launcher
├── start-editor.ps1        # PowerShell launcher
├── DISTRIBUTION.md         # Distribution guide
└── fonts/                  # IDE font files
```

---

## � Distribution & Standalone Options

See [DISTRIBUTION.md](DISTRIBUTION.md) for detailed instructions on:
- Running with `run-ide.bat` (Windows, easiest)
- Building a standalone `.exe` executable
- Running the REPL interpreter
- Different deployment options

---

## �📖 Version History

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
