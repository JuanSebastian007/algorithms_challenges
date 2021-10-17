def calc_fib(n):
    """""
    A function that computing a Fibonacci Series in a way that successive executing a sum.

    Params
    n: Number that runs Fibonacci Serie. Type: Integer.
    """
    if (n <= 1):
        return n
    
    else:
        previus = 0
        current = 1
        for _ in range (n -1):
            previus, current = current, previus + current
        return current


n = int(input()) #Number that runs Fibonacci Serie
print(calc_fib(n))