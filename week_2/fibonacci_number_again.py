# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    """""
    A function that computing the Pisano period to a specifics Fibonacci Number and moduele.

    Params
    n: Number to divided. Type: Integer.
    m: Number to divided. Type: Integer.
    """
    curr, prev = 1,0
    for i in range(m*m+1): ##The maximum length to find Pisano Period is this length
        prev,curr =  curr, (curr+prev)%m
        if (prev, curr) == (0,1): #The Pisano Period by definition, always starts with 0 and 1.
            time_period = i+1 #Due to we are registered the array with before step, We should added one step to Pisano Period length.
            break
        
    index = n%time_period #These are the steps that we need to complete the Pisano Period
    if index<1: #If We need just one steps, so the Pisana Period is 0 and 1
        return index
    prev,curr = 0,1
    for i in range(2, index+1): #Computing the Pisano Period according its length
        prev,curr = curr, (curr+prev)%m
    return curr

if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))