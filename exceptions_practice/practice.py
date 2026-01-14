try:
    x = int(input("X = "))
except ValueError:
    print("Error")
z = x + 1 # when one condition is correct, the codes will jump out of the condition and align with "try" or "except".
print(z)