
import random
import math


def crear_lista_tamaio():
    tamaio = int(input("Ingrese el tamaño de la lista: "))
    lista_numeros = []
    for i in range(tamaio):
        numero = random.randint(1, 55)
        lista_numeros.append(numero)
    return lista_numeros


def obtener_raices(lista_numeros):
    raices = []
    for num in lista_numeros:
        raiz = math.sqrt(num)
        raices.append(raiz)
    return raices
