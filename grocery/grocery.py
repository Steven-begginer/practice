# this method is to use dictionary to store and update the data. That is so interesting!
def count_item(x):
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
    return (f"{dic[x]}: {x}")

dic = {}
def main():
    while True:
        try:
            x = input("")
            count_item(x)
        except EOFError:
            for item in sorted(dic):
                print(f"{dic[item]}: {item}")
            break

if __name__ == "__main__":
    main()

