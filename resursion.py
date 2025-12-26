def main():
    height = int(input())
    draw(height)

def draw(n):
    if n == 0:
        return
    draw(n-2)
    print("#"* n)
if __name__ == "__main__":
    main()
# recursion method: it solve problems from complex to simple one. using the 