import random
def main():
    get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 0
        while tries < 3:
            try:
                answer = int(input(f" {x} + {y} = "))
                if answer == x + y:
                    score +=1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")
def get_level():
    global n
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if 1 <= n <= 3:
                return n
            else:
                continue
                

def generate_integer(n):
    if n == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10**(n-1), 10**n -1)


if __name__ == "__main__":
    main()