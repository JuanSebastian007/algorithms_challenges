# Uses python3
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

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd(a, b))