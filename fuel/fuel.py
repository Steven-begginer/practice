def calculator(f):
    if f == 0:
        return ("E")
    elif f == 1:
        return ("F")
    else:
        return (f"{int(f * 100)}%")

while True:
    fraction = input("fraction: ")
    try:
        X, Y = map(int, fraction.split("/"))
    except ValueError:
        print("Prompt the user again.")
        continue
    except ZeroDivisionError:
        print("Prompt the user again.")
        continue
    if X > Y or X / Y < 0:
        print("Prompt the user again.")
        continue
    else:
        Z = X / Y
        break
def main():
    print(calculator(Z))
main()