#Uses python3
import sys

def gcd(a, b):
    """""
    A function that computing the mcd.

    Params
    a: Number to divided. Type: Integer.
    b: Number to divided. Type: Integer.
    """
    num = max(a, b)
    dem = min(a, b) 
    if num%dem == 0:
        return dem
    
    return gcd(dem, num%dem)

def lcm_naive(a, b):
    """""
    A function that computing the lcm.

    Params
    a: Number to divided. Type: Integer.
    b: Number to divided. Type: Integer.
    """
    dem= min(a,b)
    if dem ==0: # The zero just have zero as like lcm
        return 0
    return int((a*b)/gcd(a,b))

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))