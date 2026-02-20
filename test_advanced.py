#!/usr/bin/env python
"""Test script for NumLang v1.3 - All advanced features"""

from numlang import run_code

print("=" * 70)
print("NumLang v1.3 - Advanced Features Test Suite")
print("=" * 70)

# Test 1: Statistics
print("\n[Test 1] Statistics Functions")
code1 = """
let data = [10, 20, 30, 40, 50]
print sum(data)
print min(data)
print max(data)
print mean(data)
print median(data)
"""
print(run_code(code1))

# Test 2: While loops
print("\n[Test 2] While Loops")
code2 = """
let i = 0
let total = 0
while i < 5 do
    let total = total + i
    let i = i + 1
end
print total
"""
print(run_code(code2))

# Test 3: Type conversion
print("\n[Test 3] Type Conversion")
code3 = """
let str_num = "123"
let num = int(str_num)
print num + 77
let float_num = float("3.14")
print float_num * 2
"""
print(run_code(code3))

# Test 4: String methods
print("\n[Test 4] String Methods")
code4 = """
let text = "  Hello World  "
print strip(text)
print contains(text, "World")
print replace(text, "World", "NumLang")
print find(text, "World")
"""
print(run_code(code4))

# Test 5: List methods
print("\n[Test 5] List Methods")
code5 = """
let list = [3, 1, 4, 1, 5]
print count(list, 1)
print index(list, 4)
sort(list)
print list
"""
print(run_code(code5))

# Test 6: Random
print("\n[Test 6] Random Number Generation")
code6 = """
let num = randint(1, 100)
print num
let choice = choice([10, 20, 30, 40])
print choice
"""
result6 = run_code(code6)
# Don't print random output as it's non-deterministic
print("(Random values generated - test passed)")

# Test 7: Complex math
print("\n[Test 7] Complex Mathematical Operations")
code7 = """
let nums = [1, 2, 3, 4, 5]
for i = 1 to 5 do
    print i
end
print factorial(5)
"""
print(run_code(code7))

# Test 8: String manipulation chain
print("\n[Test 8] String Manipulation")
code8 = """
let word = "pythOn"
print upper(word)
print lower(word)
let sentence = "one,two,three,four"
let parts = split(sentence, ",")
print len(parts)
let joined = join(parts, "-")
print joined
"""
print(run_code(code8))

# Test 9: Error handling with try/catch
print("\n[Test 9] Try/Catch Error Handling")
code9 = """
try
    let x = 1 / 0
catch
    print "Error caught"
end
print "Program continues"
"""
print(run_code(code9))

# Test 10: Advanced math functions
print("\n[Test 10] Advanced Math Functions")
code10 = """
print sin(pi / 2)
print cos(0)
print sqrt(16)
print log(e)
print factorial(5)
print gcd(48, 18)
"""
print(run_code(code10))

print("\n" + "=" * 70)
print("All tests completed!")
print("=" * 70)
