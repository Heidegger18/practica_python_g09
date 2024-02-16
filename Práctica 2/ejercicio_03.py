
"""
3. Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente
"""

def ingresar_datos():
    while True:
        try:
            num1 = float(input("Ingrese un primer número: "))
            num2 = float(input("Ingrese un segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Ingrese números válidos")

def division(num1, num2):
    try:
        resultado = num1 / num2
        print("Resultado de la división: {}".format(resultado))
    except ZeroDivisionError:
        print("Error: División entre cero")

def evaluar_suma(num1, num2):
    if num1 + num2 < 0:
        print("Error: La suma de los números es negativa")

def ingresar_lista():
    lista = []
    while True:
        try:
            n = int(input("Ingrese un número para la lista (o 0 para terminar): "))
            if n == 0:
                break
            lista.append(n)
        except ValueError:
            print("Error: Ingrese un número entero")

    while True:
        try:
            indice = int(input("Ingrese el índice que desea consultar: "))
            print("Valor en el índice: {}".format(lista[indice]))
            break
        except IndexError:
            print("Error: Índice fuera de rango")
        except ValueError:
            print("Error: Ingrese un número entero como índice")

#Función principal
def main():
    while True:
        num1, num2 = ingresar_datos()
        division(num1, num2)
        evaluar_suma(num1, num2)
        ingresar_lista()

        opcion_continuar = input("¿Desea continuar? (s/n): ")
        if opcion_continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
