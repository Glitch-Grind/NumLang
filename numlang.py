import math

variables = {}
user_functions = {}

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
    
    # Trigonometry
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "deg": math.degrees,
    "rad": math.radians,
    
    # Logarithms
    "log": math.log,
    "log10": math.log10,
    "log2": math.log2,
    
    # Constants
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": float('inf'),
    "nan": float('nan')
}

def evaluate(expr, line_num=0):
    """Evaluate a mathematical expression"""
    if not expr or not expr.strip():
        return None
    
    expr = expr.strip()
    
    # Replace operators
    expr = expr.replace("^", "**")
    expr = expr.replace(" mod ", " % ")
    expr = expr.replace(" mod", " %")
    expr = expr.replace("mod ", "% ")
    
    # Replace integer division
    expr = expr.replace(" // ", " // ")
    
    try:
        # Create evaluation environment with math functions, constants, and variables
        env = {**math_env, **variables, **user_functions}
        result = eval(expr, {"__builtins__": {}}, env)
        return result
    except Exception as e:
        raise Exception(f"Line {line_num}: {str(e)}")


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
    if op == '>':
        return left > right
    elif op == '<':
        return left < right
    elif op == '>=':
        return left >= right
    elif op == '<=':
        return left <= right
    elif op == '==':
        return abs(left - right) < 1e-10  # Float comparison
    elif op == '!=':
        return abs(left - right) >= 1e-10
    return False


def run_code(code, reset_state=True):
    """
    Runs full NumLang script from IDE / Flask
    """
    global variables, user_functions
    
    # Reset state only for top-level calls
    if reset_state:
        variables = {}
        user_functions = {}
    
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
                                local_env = {**math_env, **variables, **local_vars}
                                return eval(expr.replace("^", "**"), {"__builtins__": {}}, local_env)
                            return func
                        
                        user_functions[func_name] = make_func(func_name, params, expr)
                i += 1
            
            # Variable assignment
            elif line.startswith("let "):
                parts = line[4:].split("=", 1)
                if len(parts) != 2:
                    output.append(f"Line {line_num}: Invalid let statement")
                    i += 1
                    continue
                
                name = parts[0].strip()
                expr = parts[1].strip()
                value = evaluate(expr, line_num)
                variables[name] = value
                i += 1
            
            # Print statement
            elif line.startswith("print "):
                expr = line[6:].strip()
                value = evaluate(expr, line_num)
                if value is not None:
                    output.append(str(value))
                i += 1
            
            # If statement
            elif line.startswith("if "):
                condition_str = line[3:].strip()
                
                # Check for "then" keyword
                if " then" in condition_str:
                    condition_str = condition_str.split(" then")[0].strip()
                
                condition = parse_condition(condition_str, line_num)
                is_true = check_condition(*condition)
                
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
                    if_output = run_code(if_code, reset_state=False)
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
                        loop_output = run_code(loop_code, reset_state=False)
                        if loop_output:
                            output.append(loop_output)
                    
                    i += 1
                else:
                    output.append(f"Line {line_num}: Invalid for loop syntax")
                    i += 1
            
            # End statement (handled by if/for)
            elif line == "end" or line.startswith("end "):
                i += 1
            
            else:
                output.append(f"Line {line_num}: Unknown command: {line}")
                i += 1
        
        except Exception as e:
            output.append(f"Line {line_num}: {str(e)}")
            i += 1
    
    return "\n".join(output)


#  CLI MODE
if __name__ == "__main__":
    print("NumLang v1.1")
    print("Type 'exit' to quit\n")
    
    while True:
        line = input(">>> ").strip()
        
        if line == "exit":
            break
        
        result = run_code(line)
        if result:
            print(result)
