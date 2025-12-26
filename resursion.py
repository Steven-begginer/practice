def main():
    height = int(input())
    draw(height)

def draw(n):
    if n == 0:
        return
    draw(n-1)
    print("#"* n)
if __name__ == "__main__":
    main()
# recursion method: it solves problem from complex one to simple one. Using the "call stack" stores the function(need to call multiple times). imagining it like put plates. 