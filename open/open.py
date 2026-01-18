# open, write, close functions of file.
"""
name = input("What is your name? ")

file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()
"""
"""
# the second way to do it
with open("name.txt", "r") as file:
    lines = file.readlines()
'''
Input:
File:
Alice
Bob
readline() \\\\\\\\\\\\\\
return: ['Alice\n', 'Bob\n']
'''
for line in lines:
    print("hello,", line.rstrip())
"""
"""
# It is a good method to check the print() function quickly.
help(print)
"""
with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

