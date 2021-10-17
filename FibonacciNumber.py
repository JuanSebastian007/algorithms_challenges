def calc_fib(n):
    if (n <= 1):
        return n
    
    else:
        previus = 0
        current = 1
        for _ in range (n -1):
            previus, current = current, previus + current
        return current


n = int(input())
print(calc_fib(n))