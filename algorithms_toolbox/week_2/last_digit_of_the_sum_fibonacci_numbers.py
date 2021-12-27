
# Uses python3
import sys

def fibonacci_sum_last_digit(n):
    """""
    A function that computing the last digit to Fibonacci Serie sum.

    Params
    n: Number that runs Fibonacci Serie. Type: Integer.
    """
    time_period = 60 # The Pisano Period lenght to module 10 is 60
    index = n%time_period #The reminder to complete the Pisano Period
    if index<1:
        return index
    prev,curr = 0,1
    sum     = 1
    for i in range(2, index+1):
        prev,curr = curr, (curr+prev)%10
        sum = (sum + curr)%10
    return sum


if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_last_digit(n))