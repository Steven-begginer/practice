try:
    x = int(input("What's x? ")) # analyze the "success" or "failure" of assigning the value to x
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
# try - except -else : exception handling mechanism.
# understand when and where the condition has finished as an very important thing for programmers.
"""
#short version
try:
    x = int(input("What's x? ")) # analyze the "success" or "failure" of assigning the value to x
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
"""
