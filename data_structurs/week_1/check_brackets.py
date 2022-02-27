# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Si es alguna apertura, creo la tupa y la agrego a la lista. 
            bracket = Bracket(next, i)
            opening_brackets_stack.append(bracket)

        if next in ")]}":
            # Si el valor es una clausura. Si el stack esta vacio, termino el loop. Si no esta vacio, tomo el top del stack y verifico que lo que se abrio se cierre, si cumple termino el loop
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            # Busco se el bracket de apertura ha sido cerrado. Si es asi, termino el ciclo
            if (top.char == '(' and next != ')') or (top.char == '[' and next != ']') or (top.char == '{' and next != '}'):
                return i + 1
    # Retorno la posicion del bracket incorrecto
    if opening_brackets_stack:
            return opening_brackets_stack[0].position + 1
    # Exito porque los brackets han sido cerrados
    return "Success"



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
