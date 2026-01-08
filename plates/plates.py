def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def rule(s):
    for i in range(len(s)):
        if "0" <= s[i] <= "9":
            if s[i] == "0":
                return False
            for j in range(i+1, len(s)):
                if "0" <= s[j] <= "9":
                    continue
                else:
                    return False
        else:
            continue
    return True

def is_valid(s):
    if 2 <= len(s) <= 6:
        for i in range(0,2):
            if "A" <= s[i] <= "Z":
                continue
        return rule(s)
    else:
        return False
    

main()