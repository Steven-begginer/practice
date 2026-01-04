def practice(i: str) -> None:
    print("should i get an output?")
    if len(i) != 0:
        print("Y")
    else:
        print("N")





# main functions triggered place
def main():
    i = input("")  # Remove int() to get a string
    print(practice(i)) # understand when the function finished, it will return None by default if we do not set the return value explicitly.

__name__ = main()# start the program from here.

