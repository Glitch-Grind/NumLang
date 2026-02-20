import math
import os
import json
import traceback
import random
import statistics

variables = {}
user_functions = {}
debug_mode = False
call_stack = []

# Allowed math functions & constants
math_env = {
    # Basic math
    "sqrt": math.sqrt,
    "abs": abs,
    "floor": math.floor,
    "ceil": math.ceil,
    "round": round,
    "exp": math.exp,
    "pow": pow,
    "fabs": math.fabs,
    "factorial": math.factorial,
    "gcd": math.gcd,
    "lcm": math.lcm,
    
    # Trigonometry
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "atan2": math.atan2,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "deg": math.degrees,
    "rad": math.radians,
    
    # Logarithms & exponents
    "log": math.log,
    "log10": math.log10,
    "log2": math.log2,
    "log1p": math.log1p,
    
    # Constants
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": float('inf'),
    "nan": float('nan')
}

# Built-in functions for strings and lists
class NumLangList(list):
    """Custom list class for NumLang"""
    def append(self, item):
        super().append(item)
        return self
    
    def pop(self, index=-1):
        if abs(index) > len(self):
            raise IndexError(f"List index out of range")
        return super().pop(int(index))
    
    def len(self):
        return len(self)

def builtin_len(obj):
    """Get length of string or list"""
    if isinstance(obj, (str, list)):
        return len(obj)
    raise TypeError(f"object of type '{type(obj).__name__}' has no len()")

def builtin_append(lst, item):
    """Append to list"""
    if isinstance(lst, list):
        lst.append(item)
        return lst
    raise TypeError(f"append() method only works on lists")

def builtin_pop(lst, index=-1):
    """Pop from list"""
    if isinstance(lst, list):
        if abs(index) > len(lst):
            raise IndexError(f"List index out of range")
        return lst.pop(int(index))
    raise TypeError(f"pop() method only works on lists")

def builtin_upper(s):
    """Convert string to uppercase"""
    if isinstance(s, str):
        return s.upper()
    raise TypeError(f"upper() method only works on strings")

def builtin_lower(s):
    """Convert string to lowercase"""
    if isinstance(s, str):
        return s.lower()
    raise TypeError(f"lower() method only works on strings")

def builtin_split(s, sep=" "):
    """Split string"""
    if isinstance(s, str):
        return NumLangList(s.split(sep))
    raise TypeError(f"split() method only works on strings")

def builtin_join(lst, sep=""):
    """Join list of strings"""
    if isinstance(lst, list):
        return sep.join(str(x) for x in lst)
    raise TypeError(f"join() method only works on lists")

def builtin_read_file(filename):
    """Read file contents"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")

def builtin_write_file(filename, content):
    """Write to file"""
    try:
        with open(filename, 'w') as f:
            f.write(str(content))
        return True
    except Exception as e:
        raise Exception(f"Error writing file: {str(e)}")

def builtin_append_file(filename, content):
    """Append to file"""
    try:
        with open(filename, 'a') as f:
            f.write(str(content))
        return True
    except Exception as e:
        raise Exception(f"Error appending to file: {str(e)}")

# ========== STATISTICS FUNCTIONS ==========
def builtin_sum(lst):
    """Sum of list elements"""
    if isinstance(lst, list):
        return sum(lst)
    raise TypeError(f"sum() requires a list")

def builtin_min(lst):
    """Minimum value in list"""
    if isinstance(lst, list) and len(lst) > 0:
        return min(lst)
    raise ValueError(f"min() requires non-empty list")

def builtin_max(lst):
    """Maximum value in list"""
    if isinstance(lst, list) and len(lst) > 0:
        return max(lst)
    raise ValueError(f"max() requires non-empty list")

def builtin_mean(lst):
    """Average of list elements"""
    if isinstance(lst, list) and len(lst) > 0:
        return statistics.mean(lst)
    raise ValueError(f"mean() requires non-empty list")

def builtin_median(lst):
    """Median of list elements"""
    if isinstance(lst, list) and len(lst) > 0:
        return statistics.median(lst)
    raise ValueError(f"median() requires non-empty list")

def builtin_stdev(lst):
    """Standard deviation of list"""
    if isinstance(lst, list) and len(lst) > 1:
        return statistics.stdev(lst)
    raise ValueError(f"stdev() requires list with at least 2 elements")

def builtin_avg(lst):
    """Alias for mean"""
    return builtin_mean(lst)

# ========== RANDOM NUMBER FUNCTIONS ==========
def builtin_random():
    """Random float between 0 and 1"""
    return random.random()

def builtin_randint(a, b):
    """Random integer between a and b (inclusive)"""
    return random.randint(int(a), int(b))

def builtin_choice(lst):
    """Random choice from list"""
    if isinstance(lst, list) and len(lst) > 0:
        return random.choice(lst)
    raise ValueError(f"choice() requires non-empty list")

def builtin_shuffle(lst):
    """Shuffle a list in-place"""
    if isinstance(lst, list):
        random.shuffle(lst)
        return lst
    raise TypeError(f"shuffle() requires a list")

# ========== TYPE CONVERSION ==========
def builtin_int(val):
    """Convert to integer"""
    try:
        return int(float(str(val)))
    except:
        raise ValueError(f"Cannot convert {val} to integer")

def builtin_float(val):
    """Convert to float"""
    try:
        return float(val)
    except:
        raise ValueError(f"Cannot convert {val} to float")

def builtin_str(val):
    """Convert to string"""
    return str(val)

def builtin_bool(val):
    """Convert to boolean"""
    if isinstance(val, (int, float)):
        return val != 0
    elif isinstance(val, str):
        return val.lower() in ('true', '1', 'yes')
    return bool(val)

# ========== ADVANCED STRING METHODS ==========
def builtin_replace(s, old, new):
    """Replace substring"""
    if isinstance(s, str):
        return s.replace(old, new)
    raise TypeError(f"replace() requires a string")

def builtin_strip(s):
    """Remove whitespace from ends"""
    if isinstance(s, str):
        return s.strip()
    raise TypeError(f"strip() requires a string")

def builtin_startswith(s, prefix):
    """Check if string starts with prefix"""
    if isinstance(s, str):
        return s.startswith(prefix)
    raise TypeError(f"startswith() requires a string")

def builtin_endswith(s, suffix):
    """Check if string ends with suffix"""
    if isinstance(s, str):
        return s.endswith(suffix)
    raise TypeError(f"endswith() requires a string")

def builtin_contains(s, substr):
    """Check if string contains substring"""
    if isinstance(s, str):
        return substr in s
    raise TypeError(f"contains() requires a string")

def builtin_find(s, substr):
    """Find index of substring (-1 if not found)"""
    if isinstance(s, str):
        return s.find(substr)
    raise TypeError(f"find() requires a string")

# ========== ADVANCED LIST METHODS ==========
def builtin_reverse(lst):
    """Reverse a list in-place"""
    if isinstance(lst, list):
        lst.reverse()
        return lst
    raise TypeError(f"reverse() requires a list")

def builtin_sort(lst):
    """Sort a list in-place"""
    if isinstance(lst, list):
        try:
            lst.sort()
            return lst
        except:
            raise ValueError(f"Cannot sort list with incompatible types")
    raise TypeError(f"sort() requires a list")

def builtin_clear(lst):
    """Clear a list"""
    if isinstance(lst, list):
        lst.clear()
        return lst
    raise TypeError(f"clear() requires a list")

def builtin_count(lst, item):
    """Count occurrences in list"""
    if isinstance(lst, list):
        return lst.count(item)
    raise TypeError(f"count() requires a list")

def builtin_index_of(lst, item):
    """Find index of item (-1 if not found)"""
    if isinstance(lst, list):
        try:
            return lst.index(item)
        except ValueError:
            return -1
    raise TypeError(f"index() requires a list")

def builtin_range_list(start, end):
    """Create list of integers from start to end"""
    return NumLangList(range(int(start), int(end) + 1))

builtin_functions = {
    "len": builtin_len,
    "append": builtin_append,
    "pop": builtin_pop,
    
    # String methods
    "upper": builtin_upper,
    "lower": builtin_lower,
    "split": builtin_split,
    "join": builtin_join,
    "replace": builtin_replace,
    "strip": builtin_strip,
    "startswith": builtin_startswith,
    "endswith": builtin_endswith,
    "contains": builtin_contains,
    "find": builtin_find,
    
    # List methods
    "reverse": builtin_reverse,
    "sort": builtin_sort,
    "clear": builtin_clear,
    "count": builtin_count,
    "index": builtin_index_of,
    "range": builtin_range_list,
    
    # Statistics
    "sum": builtin_sum,
    "min": builtin_min,
    "max": builtin_max,
    "mean": builtin_mean,
    "avg": builtin_avg,
    "median": builtin_median,
    "stdev": builtin_stdev,
    
    # Random
    "random": builtin_random,
    "randint": builtin_randint,
    "choice": builtin_choice,
    "shuffle": builtin_shuffle,
    
    # Type conversion
    "int": builtin_int,
    "float": builtin_float,
    "str": builtin_str,
    "bool": builtin_bool,
    
    # File I/O
    "read_file": builtin_read_file,
    "write_file": builtin_write_file,
    "append_file": builtin_append_file,
}

def evaluate(expr, line_num=0):
    """Evaluate a mathematical expression, string, or list operation"""
    if not expr or not expr.strip():
        return None
    
    expr = expr.strip()
    
    # Handle string literals
    if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
        quote = expr[0]
        return expr[1:-1]
    
    # Handle list literals [1, 2, 3]
    if expr.startswith('[') and expr.endswith(']'):
        try:
            list_content = expr[1:-1].strip()
            if not list_content:
                return NumLangList()
            items = [evaluate(item.strip(), line_num) for item in list_content.split(',')]
            return NumLangList(items)
        except Exception as e:
            raise Exception(f"Line {line_num}: Invalid list literal - {str(e)}")
    
    # Replace operators
    expr = expr.replace("^", "**")
    expr = expr.replace(" mod ", " % ")
    expr = expr.replace(" mod", " %")
    expr = expr.replace("mod ", "% ")
    expr = expr.replace(" // ", " // ")
    
    # Handle string concatenation with .
    if " . " in expr:
        parts = expr.split(" . ")
        result = ""
        for part in parts:
            val = evaluate(part.strip(), line_num)
            result += str(val)
        return result
    
    try:
        # Create evaluation environment
        env = {**math_env, **builtin_functions, **variables, **user_functions}
        result = eval(expr, {"__builtins__": {}}, env)
        return result
    except Exception as e:
        error_msg = str(e)
        if debug_mode:
            error_msg += f"\nCall stack: {' -> '.join(call_stack)}" if call_stack else ""
        raise Exception(f"Line {line_num}: {error_msg}")


def parse_condition(condition_str, line_num):
    """Parse a condition and return (left, operator, right)"""
    operators = ['>=', '<=', '==', '!=', '>', '<']
    
    for op in operators:
        if op in condition_str:
            parts = condition_str.split(op, 1)
            if len(parts) == 2:
                left = evaluate(parts[0].strip(), line_num)
                right = evaluate(parts[1].strip(), line_num)
                return (left, op, right)
    
    raise Exception(f"Line {line_num}: Invalid condition: {condition_str}")


def check_condition(left, op, right):
    """Check if a condition is true"""
    try:
        if op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '>=':
            return left >= right
        elif op == '<=':
            return left <= right
        elif op == '==':
            # Float comparison for numbers, direct comparison for others
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return abs(left - right) < 1e-10
            return left == right
        elif op == '!=':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return abs(left - right) >= 1e-10
            return left != right
        return False
    except Exception as e:
        raise Exception(f"Cannot compare {type(left).__name__} and {type(right).__name__}: {str(e)}")


def run_code(code, reset_state=True, debug=False):
    """
    Runs full NumLang script from IDE / Flask
    Supports variables, functions, control flow, lists, strings, and file I/O
    """
    global variables, user_functions, debug_mode, call_stack
    
    debug_mode = debug
    
    # Reset state only for top-level calls
    if reset_state:
        variables = {}
        user_functions = {}
        call_stack = []
    
    output = []
    lines = code.split("\n")
    line_num = 0
    
    i = 0
    while i < len(lines):
        line_num = i + 1
        line = lines[i].strip()
        
        try:
            if not line or line.startswith("#"):
                i += 1
                continue
            
            # Debug output
            if debug_mode and line and not line.startswith("#"):
                output.append(f"[DEBUG] Line {line_num}: {line}")
            
            # User-defined function
            elif line.startswith("function "):
                func_line = line[9:].strip()
                if "=" in func_line:
                    # Simple function: function name(x) = expression
                    parts = func_line.split("=", 1)
                    func_def = parts[0].strip()
                    expr = parts[1].strip()
                    
                    # Parse function name and parameters
                    if "(" in func_def and ")" in func_def:
                        name_part = func_def[:func_def.index("(")]
                        params_part = func_def[func_def.index("(")+1:func_def.index(")")]
                        func_name = name_part.strip()
                        params = [p.strip() for p in params_part.split(",") if p.strip()]
                        
                        # Create a lambda function
                        def make_func(func_name, params, expr):
                            def func(*args):
                                if len(args) != len(params):
                                    raise Exception(f"Function {func_name} expects {len(params)} arguments, got {len(args)}")
                                # Create local scope with parameters
                                local_vars = dict(zip(params, args))
                                local_env = {**math_env, **builtin_functions, **variables, **local_vars, **user_functions}
                                return eval(expr.replace("^", "**"), {"__builtins__": {}}, local_env)
                            return func
                        
                        user_functions[func_name] = make_func(func_name, params, expr)
                        if debug_mode:
                            output.append(f"[DEBUG] Defined function: {func_name}({', '.join(params)})")
                i += 1
            
            # Variable assignment
            elif line.startswith("let "):
                parts = line[4:].split("=", 1)
                if len(parts) != 2:
                    raise Exception(f"Invalid let statement")
                
                name = parts[0].strip()
                expr = parts[1].strip()
                value = evaluate(expr, line_num)
                variables[name] = value
                
                if debug_mode:
                    output.append(f"[DEBUG] Set {name} = {value}")
                i += 1
            
            # Print statement
            elif line.startswith("print "):
                expr = line[6:].strip()
                value = evaluate(expr, line_num)
                if value is not None:
                    output.append(str(value))
                i += 1
            
            # Debug command: show variables
            elif line == "debug" or line == "vars":
                output.append("[DEBUG] Current variables:")
                for var_name, var_val in variables.items():
                    output.append(f"  {var_name} = {var_val}")
                i += 1
            
            # If statement
            elif line.startswith("if "):
                condition_str = line[3:].strip()
                
                # Check for "then" keyword
                if " then" in condition_str:
                    condition_str = condition_str.split(" then")[0].strip()
                
                condition = parse_condition(condition_str, line_num)
                is_true = check_condition(*condition)
                
                if debug_mode:
                    output.append(f"[DEBUG] Condition {condition_str} = {is_true}")
                
                # Find the matching "end"
                if_block = []
                i += 1
                depth = 1
                
                while i < len(lines) and depth > 0:
                    current_line = lines[i].strip()
                    if current_line.startswith("if "):
                        depth += 1
                    elif current_line == "end" or current_line.startswith("end "):
                        depth -= 1
                        if depth == 0:
                            break
                    
                    if depth > 0:
                        if_block.append(lines[i])
                    i += 1
                
                if is_true:
                    # Execute the if block (don't reset state)
                    if_code = "\n".join(if_block)
                    if_output = run_code(if_code, reset_state=False, debug=debug_mode)
                    if if_output:
                        output.append(if_output)
                
                i += 1
            
            # For loop
            elif line.startswith("for "):
                loop_line = line[4:].strip()
                
                # Parse: for i = 1 to 10 do
                if "=" in loop_line and " to " in loop_line and " do" in loop_line:
                    parts = loop_line.split(" do")[0]
                    var_part, range_part = parts.split(" to ", 1)
                    var_name = var_part.split("=")[0].strip()
                    start_expr = var_part.split("=")[1].strip()
                    end_expr = range_part.strip()
                    
                    start_val = int(evaluate(start_expr, line_num))
                    end_val = int(evaluate(end_expr, line_num))
                    
                    if debug_mode:
                        output.append(f"[DEBUG] Loop: {var_name} from {start_val} to {end_val}")
                    
                    # Find the matching "end"
                    loop_block = []
                    i += 1
                    depth = 1
                    
                    while i < len(lines) and depth > 0:
                        current_line = lines[i].strip()
                        if current_line.startswith("for "):
                            depth += 1
                        elif current_line == "end" or current_line.startswith("end "):
                            depth -= 1
                            if depth == 0:
                                break
                        
                        if depth > 0:
                            loop_block.append(lines[i])
                        i += 1
                    
                    # Execute loop (don't reset state)
                    loop_code = "\n".join(loop_block)
                    for val in range(start_val, end_val + 1):
                        variables[var_name] = val
                        loop_output = run_code(loop_code, reset_state=False, debug=debug_mode)
                        if loop_output:
                            output.append(loop_output)
                    
                    i += 1
                else:
                    raise Exception(f"Invalid for loop syntax. Expected: for var = start to end do")
            
            # While loop
            elif line.startswith("while "):
                condition_str = line[6:].strip()
                
                # Check for "do" keyword
                if " do" in condition_str:
                    condition_str = condition_str.split(" do")[0].strip()
                
                # Find the matching "end"
                while_block = []
                i += 1
                depth = 1
                
                while i < len(lines) and depth > 0:
                    current_line = lines[i].strip()
                    if current_line.startswith("while "):
                        depth += 1
                    elif current_line == "end" or current_line.startswith("end "):
                        depth -= 1
                        if depth == 0:
                            break
                    
                    if depth > 0:
                        while_block.append(lines[i])
                    i += 1
                
                # Execute while loop (don't reset state)
                while_code = "\n".join(while_block)
                max_iterations = 100000  # Prevent infinite loops
                iteration = 0
                
                while iteration < max_iterations:
                    try:
                        condition = parse_condition(condition_str, line_num)
                        is_true = check_condition(*condition)
                    except:
                        is_true = False
                    
                    if not is_true:
                        break
                    
                    loop_output = run_code(while_code, reset_state=False, debug=debug_mode)
                    if loop_output:
                        output.append(loop_output)
                    iteration += 1
                
                if iteration >= max_iterations:
                    output.append(f"ERROR: Line {line_num}: While loop exceeded maximum iterations ({max_iterations})")
                
                i += 1
            
            # Try/Catch error handling
            elif line.startswith("try"):
                # Find the matching "catch"
                try_block = []
                i += 1
                
                while i < len(lines):
                    current_line = lines[i].strip()
                    if current_line.startswith("catch"):
                        break
                    try_block.append(lines[i])
                    i += 1
                
                # Find catch block
                catch_block = []
                if i < len(lines) and lines[i].strip().startswith("catch"):
                    i += 1
                    while i < len(lines):
                        current_line = lines[i].strip()
                        if current_line == "end" or current_line.startswith("end "):
                            break
                        catch_block.append(lines[i])
                        i += 1
                
                # Execute try block
                try_code = "\n".join(try_block)
                try:
                    try_output = run_code(try_code, reset_state=False, debug=debug_mode)
                    if try_output and not try_output.startswith("ERROR"):
                        output.append(try_output)
                except Exception as e:
                    # Execute catch block
                    if catch_block:
                        # Set error variable
                        variables["error"] = str(e)
                        catch_code = "\n".join(catch_block)
                        catch_output = run_code(catch_code, reset_state=False, debug=debug_mode)
                        if catch_output:
                            output.append(catch_output)
                
                i += 1
            
            # End statement (handled by if/for/while)
            elif line == "end" or line.startswith("end "):
                i += 1
            
            else:
                # Try to evaluate as an expression statement
                try:
                    result = evaluate(line, line_num)
                    # Don't print expression results unless they're meaningful
                    # This allows for statements like: append(list, item)
                except Exception as expr_error:
                    raise Exception(f"Unknown command: {line}")
                
                i += 1
        
        except Exception as e:
            error_str = str(e)
            if not error_str.startswith("Line"):
                error_str = f"Line {line_num}: {error_str}"
            output.append(f"ERROR: {error_str}")
            if debug_mode:
                output.append(traceback.format_exc())
            i += 1
    
    return "\n".join(output)


#  REPL / CLI MODE with interactive debugging
if __name__ == "__main__":
    print("=" * 50)
    print("NumLang v1.2 - Interactive REPL")
    print("=" * 50)
    print("Commands:")
    print("  exit          - Quit the interpreter")
    print("  clear         - Clear all variables")
    print("  vars / debug  - Show all variables")
    print("  debug on/off  - Toggle debug mode")
    print("  help          - Show language features")
    print("=" * 50 + "\n")
    
    debug_enabled = False
    
    while True:
        try:
            line = input(">>> ").strip()
            
            if not line:
                continue
            
            if line == "exit":
                print("Goodbye!")
                break
            
            elif line == "clear":
                variables.clear()
                user_functions.clear()
                print("Cleared all variables and functions")
            
            elif line == "vars" or line == "debug":
                if variables:
                    print("[Variables]")
                    for var_name, var_val in variables.items():
                        print(f"  {var_name} = {var_val}")
                else:
                    print("No variables defined")
                
                if user_functions:
                    print("[Functions]")
                    for func_name in user_functions.keys():
                        print(f"  {func_name}")
                else:
                    print("No functions defined")
            
            elif line.startswith("debug "):
                cmd = line[6:].strip().lower()
                if cmd == "on":
                    debug_enabled = True
                    print("Debug mode: ON")
                elif cmd == "off":
                    debug_enabled = False
                    print("Debug mode: OFF")
            
            elif line == "help":
                print("""
NumLang Features:
  Variables:     let x = 10
  Print:         print x
  Functions:     function square(x) = x * x
  Conditionals:  if x > 5 then ... end
  Loops:         for i = 1 to 10 do ... end
  
  Lists:         [1, 2, 3], len(list), append(list, item)
  Strings:       "hello", upper("text"), lower("TEXT")
  
  File I/O:      read_file("file.txt"), write_file("file.txt", "content")
  
  Math:          sqrt, sin, cos, tan, log, exp, pow
  Math Consts:   pi, e, tau, inf, nan
                """)
            
            else:
                result = run_code(line, reset_state=False, debug=debug_enabled)
                if result and not result.startswith("[DEBUG]"):
                    print(result)
                elif debug_enabled and result:
                    print(result)
        
        except KeyboardInterrupt:
            print("\nInterrupted")
        except Exception as e:
            print(f"ERROR: {str(e)}")
