import random

def genlist():
    lista = [random.randint(0, 100) for _ in range(10)]
    return lista

def mostlist(lista):
    print("La lista generada es:", lista)
