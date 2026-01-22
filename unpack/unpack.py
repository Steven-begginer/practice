#first, last = input("What is your name? ").split(" ")
#print(f"hello, {first}")
def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins1 = [100, 50, 25] #data type: list
coins2 = {"galleons": 100, "sickles": 50, "knuts": 25} #data type： dict
print(total(*coins1), "Knuts") #unpacking the coins list
print(total(**coins2), "Knuts") #unpacking the coins dictionary


