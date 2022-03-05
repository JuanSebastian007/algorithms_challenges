# python3


class MinHeap:
    # Defino el min heap como una clase con las propiedades del array y el tamaño del array
    def __init__(self, array):
        self.A = array
        self.size = len(self.A)
        self.swaps = []

    def SiftDown(self, i):
        """""
        Funcion que va intercambiando la posicion dada por su hijo menor, 
        hasta que sea mayor a sus dos hijos.
        """
        min_index = i
        left = 2 * i + 1  # left child
        right = 2 * i + 2  # right child
        # Hago la comparacion del nodo padre con sus dos hijos y asigno el nodo menor, es un min-heap, entre los
        if left < self.size and self.A[left] < self.A[min_index]:
            min_index = left
        if right < self.size and self.A[right] < self.A[min_index]:
            min_index = right
        # Si el i cambio, entonces asigno el cambio en el arbol y en el array que va asignando la lista de cambios.
        if min_index != i:
            self.swaps.append((i, min_index))
            self.A[i], self.A[min_index] = self.A[min_index], self.A[i]
            self.SiftDown(min_index)

    def BuildHeap(self):
        n = self.size
        for i in range(n // 2 - 1, -1, -1):
            self.SiftDown(i)


def main():
    n = int(input())
    array = list(map(int, input().split()))
    assert len(array) == n

    heap = MinHeap(array)
    MinHeap.BuildHeap(heap)
    swaps = heap.swaps
    print(len(swaps))
    for swap in swaps:
        print(*swap)


if __name__ == "__main__":
    main()
