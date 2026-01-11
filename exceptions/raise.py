while True:
    try:
        x = int(input("What's x? "))
        print(f"x is {x}")
        break
    except ValueError:
        print("I caught the error, but I still want to stop everything now.")
        # Re-raises the exact same ValueError that was just caught:
        raise