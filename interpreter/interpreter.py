def calculator(x, y, z):
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    else:
        y == "/"
        if z == 0:
            return False
        else:
            return float(x / z)
def main():
    expression = input(f"Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    print(calculator(x, y, z))

main()
