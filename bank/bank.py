# balance is global variable , but it only can read in local function, if we want to modify the global variable, it should be declare by using "global" argument.
"""
balance = 0
def main():
    print(f"balance: {balance}")
    deposite(100)
    withdraw(50)
    print(f"blance: {balance}")

def deposite(n):
    global balance
    balance += n

def withdraw(n):
    global balance 
    balance -= n

if __name__ == "__main__":
    main()
"""
#build the private attributes to build the internal mechanism stability. can not modify and access it at outer class.like account.balance as public attribute.
class Account:
    def __init__(self):
        self._balance = 0 #private attribute
    
    @property 
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n

account = Account()
print(account.balance())
account.deposit(100)
account.withdraw(50)
print(account.balance())
