vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

def main():
    Input = input("Input: ")
    print(short(Input))

def short(I):
    result = ''
    for i in I:
        if i not in vowels:
            result += i
    return f"Output: {result}"

if __name__ == "__main__":
    main()
