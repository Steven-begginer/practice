def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# underlying understand why i need to use the __name__ == "__main__" connected to say.py.
# since the python will execute the codes from top to bottom, left to right. 
#if we do not use under conditions , it will automactically execute both two .py files together.
if __name__ == "__main()":
    main()