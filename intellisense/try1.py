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

total_bits = int(input("Input a number of bits: "))
bytes = total_bits // 8
remaining_bits = total_bits % 8
kb = bytes // 1024
remaining_bytes = bytes % 1024
mb = kb // 1024
remaining_kb = kb % 1024
print(f"{total_bits} b = {mb} MB {remaining_kb} KB {remaining_bytes} B {remaining_bits} b")
