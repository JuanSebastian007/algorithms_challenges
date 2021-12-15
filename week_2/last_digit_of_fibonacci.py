# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    """""
    A function that computing a the last digit from Fibonacci Series in a way that successive executing a sum.

    Params
    n: Number that runs Fibonacci Serie. Type: Integer.
    """
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10 #Its more efficiently  to compute the last digit at the for loop.

    return current

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))