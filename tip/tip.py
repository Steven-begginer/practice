def dollars_to_float(d):
    d = float(d.replace("$", ""))
    print(d)
    return d

def percent_to_float(p):
    p = float(int((p.replace("%", ""))) / 100)
    print(p)
    return p

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to trip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()