def calculator(insert_coins):
    Amount_Due = 50
    while Amount_Due != 0:
        if insert_coins == 25 or insert_coins == 10 or insert_coins == 5:
            Amount_Due -= insert_coins
            print(f"Amount Due: {Amount_Due}")
            if Amount_Due == 0:
                return
            else:
                insert_coins = int(input("Insert Coin: "))
        else:
            print(f"Amount Due: {Amount_Due}")
            insert_coins = int(input("Insert Coin: "))
            if Amount_Due == 0:
                return 

def main():
    insert_coins = int(input("Insert Coin: "))
    calculator(insert_coins)

main()
