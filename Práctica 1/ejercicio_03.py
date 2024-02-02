
"""
3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario.
"""

datos = {}

datos["nombre"] = input("Digite su nombre: ")
datos["apellidos"] = input("Digite sus apellidos: ")
datos["edad"] = int(input("Digite su edad: "))
datos["dni"] = int(input("Digite su dni: "))

valores_diccionario = list(datos.values())

print("Valores del diccionario: {}".format(valores_diccionario))

datos["profesion"] = "Ingeniería de Sistemas"

del(datos["dni"])

print("Mi nuevo diccionario es: {}".format(datos))
