# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    # Esto sirve como una especie de cache que ira guardando la posicion del numero mas grande en el recorrido.
    dq = deque()
    max_nums = []
    length = len(sequence)
    for i in range(length):
        #Yo pregunto si existe el numero actual es mayor. Si es asi, lo quito de lo mayor
        while dq and sequence[i] >= sequence[dq[-1]]:
            dq.pop()
        dq.append(i)
        # Pregunto si cumple con la condicion del contexto el numero mayor de la lista. 
        if i >= m and dq and dq[0] == i - m:
            dq.popleft()
        # Al terminar el ancho de la ventana, agrego el numero mayor que esta en la posicion 0 de la cola.
        if i >= m - 1:
            max_nums.append(sequence[dq[0]])
    return max_nums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

