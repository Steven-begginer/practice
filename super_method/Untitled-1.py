#time complexity: O(N), space complexity: O(1)
def iterative_function(n):
    if n <= 2:
        current = 1
        return current 
    elif n > 2:
        x = 1
        y = 1
        for i in range(3, n+1):
            z = x + y
            y = x
            x = z 
        return (x)


# time complexity is O(2^n), aux space is O(n)
def rec_fib(n):
    if n <= 2:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)
    
print(iterative_function(8))
print(rec_fib(8))