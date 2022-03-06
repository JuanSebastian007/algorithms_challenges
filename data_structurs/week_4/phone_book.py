# python3


class Query:
    #Creacion de la clase Queries que contendra la agenda telefonica.
    def __init__(self, query):
        self.type = query[0]
        self.number = query[1]
        if self.type == "add":
            self.name = query[2]

#Impre en consula un string que se pasa como parametro.
def WriteResponses(result):
    print('\n'.join(result))


def ProcessQuery(query, contacts):
    #Si la funcion es agregar, agrego el numero a la query. 
    if query.type == "add":
        contacts[query.number] = query.name
    #Si la funcion es eliminar, buscamos si contiene el numero y lo eliminamos.
    elif query.type == "del":
        if contacts.__contains__(query.number):
            del contacts[query.number]
    #Si no es ninguna de las anteriores, entonces es la accion de buscar. Buscamos el numero y devolvemos respuesta, sino devolvemos un not found.
    else:
        response = 'not found'
        if contacts.__contains__(query.number):
            response = contacts[query.number]
        return response


n_queries = int(input())
contacts = {}
for _ in range(n_queries):
    query = Query(input().split())
    result = ProcessQuery(query, contacts)
    if result:
        print(result)
