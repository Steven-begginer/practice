def main():
    x = int(input("What is it? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()