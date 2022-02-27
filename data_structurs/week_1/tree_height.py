# python3

import sys
import threading


def compute_height(n, parents):
    #Creea el arreglo de los niveles del arbol. En este caso es maximo el numero de elementos. Como los ire asignando, creo una lista nulla. 
    T = [None] * n
    # Como se que la raiz es en -1, busco de entrada la raiz y le asigno el nivel 1.
    root = parents.index(-1)
    T[root] = 1

    #Comienzo agregar el nivel a cada vertice del arbol. Se los agrego en orden ascendente, de 0 a 4
    for vertex in range(n):
        #Inicio en el vertice 0. Inicio el recorrido
        height = 0
        current = vertex
        # Pregunto si no estoy en la raiz
        while current != -1:
            height += 1
            #Pregunto por el padre del valor actual.
            current = parents[current]
            # Voy escalando en los padres hasta llegar a la raiz.
            if T[current]:
                T[vertex] = T[current] + height
                break
    return max(T)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
