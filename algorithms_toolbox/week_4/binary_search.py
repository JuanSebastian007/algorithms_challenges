# Uses python3
import sys

def binary_search(a, x):
    #Defino los extremos como el valor maximo y minimo del arreglo.
    left, right = 0, len(a) - 1
    
    while left <= right:
        # Tomo el punto medio del arreglo. Si el valor a encontrar es mayor que el punto medio, entonces tomo la mitad mas grande. 
        # En caso contrario, tomo la mitad mas pequeña. Si el valor medio es igual al valor a buscar, retorno el indice. 
        mid = (right + left) // 2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def linear_search(a, x):
    # Hago un recorrido linear preguntando a cada valor si el valor a encontrar.
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
