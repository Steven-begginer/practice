"""
msg = "hello world"
print(type(msg))
print(msg)
print("42,500")
val = 50 + 54
print("The final result is " + str(val))
val = "I love u"  
print(val)
print(type(True))
"""
"""
import math

x = input("Enter your first mark: ")
y = input("Enter your second mark: ")
z = math.floor((float(x) + float(y)) / 2 + 0.5)
print("Your unit mark is", int(z))
"""

bits = int(input("Input a number of bits: "))
total_bits = bits

bytes_ = bits // 8
bits = bits % 8

kb = bytes_ // 1024
bytes_ = bytes_ % 1024

mb = kb // 1024
kb = kb % 1024

print(f"{total_bits} b = {mb} MB {kb} KB {bytes_} B {bits} b")
