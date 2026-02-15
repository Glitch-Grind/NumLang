import math

variables = {}

# Allowed math functions & constants
math_env = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "pi": math.pi,
    "e": math.e
}

def evaluate(expr):
    # Replace ^ with Python power operator
    expr = expr.replace("^", "**")
    return eval(expr, {"__builtins__": {}}, {**math_env, **variables})

print("Math Language v1.0")
print("Type 'exit' to quit\n")

while True:
    try:
        line = input(">>> ").strip()

        if line == "exit":
            break

        # Ignore comments & empty lines
        if not line or line.startswith("#"):
            continue

        elif line.startswith("let "):
            # Example: let x = 5 + 3
            parts = line[4:].split("=")
            name = parts[0].strip()
            expr = parts[1].strip()

            value = evaluate(expr)
            variables[name] = value

        elif line.startswith("print "):
            expr = line[6:].strip()
            value = evaluate(expr)
            print(value)

        else:
            print("Unknown command")

    except Exception as e:
        print("Error:", e)

