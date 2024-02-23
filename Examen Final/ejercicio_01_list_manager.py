
import random


def generar_numeros_aleatorios():
    numeros_aleatorios = []
    for i in range(10):
        numero = random.randint(1, 23)
        numeros_aleatorios.append(numero)
    print("Lista de números aleatorios: {}".format(numeros_aleatorios))
    return numeros_aleatorios


def eliminar_repetidos(lista):
    numeros_no_repetidos = list(set(lista))
    print("Números no repetidos: {}".format(numeros_no_repetidos))
    return numeros_no_repetidos


def ordenar_numeros(lista):
    orden_descendente = sorted(lista, reverse=True)
    orden_ascendente = sorted(lista)
    print("Lista ordenada descendente: {}".format(orden_descendente))
    print("Lista ordenada ascendente: {}".format(orden_ascendente))
    return orden_descendente, orden_ascendente


def mayor_numero_par(lista):
    numeros_pares = []
    for num in lista:
        if num % 2 == 0:
            numeros_pares.append(num)
    if numeros_pares:
        mayor_par = max(numeros_pares)
        print("El mayor número par es: {}".format(mayor_par))
        return mayor_par
    else:
        print("No hay números pares en la lista.")
