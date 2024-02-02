
"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista.
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
#Tipos de datos
print(type(nombre))
print(type(edad))

datos_trabajadores = []
i = 0
while i < 2:
    nombre = input("Ingrese su nombre: ")
    datos_trabajadores.append(nombre)
    edad = int(input("Ingrese su edad: "))
    datos_trabajadores.append(edad)
    i += 1

#print(datos_trabajadores)

suma_edades_trabajadores = datos_trabajadores[1] + datos_trabajadores[3]
print("La suma de los trabajadores es: {}".format(suma_edades_trabajadores))
