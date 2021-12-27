# Uses python3
import sys

def get_change(m):
    """""
    Take the amoung and it divided to largest coin.
    Then, take the remainder and repeat the process with the next largest coin.
    """
    coins = [10, 5, 1] #The array should be sorted
    coins_count = 0

    for coin in coins: # Take each coin and compute integer division.
        coins_count += m // coin
        m %= coin #Update the amoung with the division reminder
    return coins_count

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
