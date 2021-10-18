
# Uses python3
import sys

def fibonacci_sum_last_digit(n):
    """""
    A function that computing the last digit to Fibonacci Serie sum.

    Params
    n: Number that runs Fibonacci Serie. Type: Integer.
    """
    time_period = 60
    index = n%time_period
    if index<1:
        return index
    prev,curr = 0,1
    sum1      = 1
    for i in range(2, index+1):
        prev,curr = curr, (curr+prev)%10
        sum1 = (sum1 + curr)%10
    return sum1


if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_last_digit(n))