#python3


import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        #Creo una cola que vaya registrando los valores maximos
        self.max_value = []

    def Push(self, a):
        # Si no hay ningun valor maximo y agrego un valor, el valor maximo sera agregado
        if not self.max_value:
            self.max_value.append(a)
        # Si el valor que quiero agregar es mayor que el valor maximo actual, lo agrego de primero al valor maximo. 
        elif a >= self.max_value[-1]:
            self.max_value.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        # Si quito un valor y este es el valor maximo, lo quito de la cola de valores maximos.
        if self.__stack[-1] == self.max_value[-1]:
            self.max_value.pop()
        self.__stack.pop()

    def Max(self):
        # Llamo al valor maximo.
        return self.max_value[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)