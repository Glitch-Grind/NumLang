#!/usr/bin/env python
"""Test script to verify all NumLang v1.2 features"""

from numlang import run_code

print("=" * 60)
print("NumLang v1.2 Feature Tests")
print("=" * 60)

# Test 1: Basic arithmetic
print("\n[Test 1] Basic Arithmetic")
code1 = """
let x = 10
let y = 20
print x + y
"""
print(run_code(code1))

# Test 2: Lists
print("\n[Test 2] Lists & List Operations")
code2 = """
let numbers = [1, 2, 3]
print len(numbers)
append(numbers, 4)
print numbers
"""
print(run_code(code2))

# Test 3: Strings
print("\n[Test 3] String Operations")
code3 = """
let greeting = "Hello"
print upper(greeting)
print lower(greeting)
let name = "World"
let message = greeting . ", " . name . "!"
print message
"""
print(run_code(code3))

# Test 4: For Loop
print("\n[Test 4] For Loops")
code4 = """
for i = 1 to 3 do
    print i
end
"""
print(run_code(code4))

# Test 5: Functions
print("\n[Test 5] User-Defined Functions")
code5 = """
function square(x) = x * x
function add(a, b) = a + b
print square(5)
print add(3, 7)
"""
print(run_code(code5))

# Test 6: Conditionals
print("\n[Test 6] Conditional Statements")
code6 = """
let score = 85
if score >= 90 then
    print "Grade: A"
end
if score >= 80 then
    print "Grade: B"
end
"""
print(run_code(code6))

# Test 7: String operations
print("\n[Test 7] String Splitting & Joining")
code7 = """
let text = "one,two,three"
let parts = split(text, ",")
print parts
let result = join(parts, "-")
print result
"""
print(run_code(code7))

# Test 8: Math functions
print("\n[Test 8] Mathematical Functions")
code8 = """
let angle = pi / 4
print sin(angle)
print cos(angle)
let sqrt_val = sqrt(16)
print sqrt_val
"""
print(run_code(code8))

print("\n" + "=" * 60)
print("All tests completed!")
print("=" * 60)
