def convert(x):
    if ":)" in x:
        x = x.replace(":)", "🙂")
        if ":(" in x:
            x = x.replace(":(", "🙁")
            return x
        return x
    elif ":(" in x:
        return x.replace(":(", "🙁")

def main():
    emoji = str(input(""))
    print(convert(emoji))
main()