def main():
    time = input("What time is it? ")
    Hour,Minutes = time.split(":")
    T = 0
    appearance = convert(Hour,Minutes,T)
    print(appearance)

def convert(H,M,T):
    if int(H) >= 7 and int(H) <= 8:
        T= calculate(H,M)
        return (f"breakfast time {T:.2f} a.m.")
    elif int(H) >= 12 and int(H) <= 13:
        if int(H) == 13:
            H = int(H) - 12
        else:
            T= calculate(H,M)
            return (f"lunch time {T:.2f} p.m.")
    elif int(H) >= 16 and int(H) <= 19:
        H = int(H) - 12
        T= calculate(H,M)
        return (f"dinner time {T:.2f} p.m.")

def calculate(H,M):
    M = int(M) / 60
    return (int(H)+ M)

if __name__ == "__main__":
    main()

# every function can implement one function!!!