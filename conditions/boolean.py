def main():
    x = int(input("what's x? "))
    if is_even(x): # if the condition is True, continue to execute the next line, otherwise, jumping to the else condition.
        print("Even")
    else:
        print("Odd")

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    # return True if x % 2 == 0 else False. (second method)
    # return (n % 2 == 0) (third method)
main()