# Uses python3
import sys
import math

def get_change(money):
    #write your code here
    denominations = [1, 3, 4]
    #Creo un arreglo del tamaño del dinero de forma ordenada. En este caso, de 0-10 e ire preguntando en cada casilla cuantas monedas son necesarias para cambiar dicho valor. 
    minCoins = [0] + [math.inf]*money
    for i in range(1, money+1):
        for j in denominations:
            if i>=j:
                coins = minCoins[i-j]+1
                if coins < minCoins[i]:
                    minCoins[i] = coins
    return minCoins[money]
if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
