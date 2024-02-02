
"""
2.Usando el concepto y funciones de listas, realizar un programa con
las siguiente características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas.
"""

lista_1 = []
for i in range(10):
    valor = int(input("Ingrese un valor {}: ".format(i+1)))
    lista_1.append(valor)

lista_cubos = []
for i in range(10):
    valor = lista_1[i] ** 3
    lista_cubos.append(valor)

lista_cuadrados = []
for i in range(10):
    valor = lista_1[i] ** 2
    lista_cuadrados.append(valor)

suma_listas = lista_cubos + lista_cuadrados
suma_listas.reverse() #Lista inversa
print(suma_listas)
