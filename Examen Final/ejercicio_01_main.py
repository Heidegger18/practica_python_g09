
"""
EJERCICIO 01

1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):
Reglas:

- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.

- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.

- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.

- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.
"""

import ejercicio_01_list_manager as lm


def main():

    # Generamos los números aleatorios
    numeros_aleatorios = lm.generar_numeros_aleatorios()

    print("---------------------------------------------------------------")

    # Eliminamos los números repetidos
    numeros_no_repetidos = lm.eliminar_repetidos(numeros_aleatorios)

    print("---------------------------------------------------------------")

    # Ordenamos los números
    orden_descendente, orden_ascendente = (
        lm.ordenar_numeros(numeros_no_repetidos))

    print("---------------------------------------------------------------")

    # Encontramos el número par mayor
    lm.mayor_numero_par(numeros_no_repetidos)


if __name__ == "__main__":
    main()
