c = 300000000

def E(m):
    return m * c ** 2

def main():
    m = int(input("m: "))
    print(f'"E: " {E(m)}')
    
main()