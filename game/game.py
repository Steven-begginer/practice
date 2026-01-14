import random
def cycle1():
    global number
    while True:
        level = input("Level: ")
        try: 
            level = int(level)
            if level < 0:
                continue
        except ValueError:
            continue
        number = random.randint(1, level)
        print(number)
        return number 

def main():
    cycle1()
    while True:
        guess = input("Guess: ")
        try: 
            guess = int(guess)
            if guess < 0:
                continue
        except ValueError:
            continue
        break
    if guess < number:
        print("Too small!")
    elif guess == number:
        print("Just right!")
    else:
        print("Too large!")

main()