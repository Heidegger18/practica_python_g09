
"""
3. (3 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.

Reglas:

- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora

- Crear una función, por ejemplo: multiplicación de 4 números (o x números)
para decorarla con la función anterior.

- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos.
"""

import time


# Definir el decorador para medir el tiempo de ejecución
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print("Tiempo de ejecución de {}: {} segundos"
              .format(func.__name__, tiempo_ejecucion))
        return resultado
    return wrapper


# Decorador para multiplicar varios números
@medir_tiempo
def multiplicar(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado


# Ejemplos de uso del decorador con la función multiplicar
resultado_1 = multiplicar(18, 3, 2)
print("Resultado de la multiplicación {}".format(resultado_1))

print("------------------------------------------------")

resultado_2 = multiplicar(4, 18, 7, 14)
print("Resultado de la multiplicación: {}".format(resultado_2))

print("------------------------------------------------")

resultado_3 = multiplicar(23, 55, 5, 2, 8)
print("Resultado de la multiplicación: {}".format(resultado_3))
