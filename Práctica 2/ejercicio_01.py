
"""
1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)
"""

import datetime

class Persona:
    def __init__(self, nombre, edad, saldo, nacionalidad):
        self.nombre = nombre
        self.edad = self.validar_edad(edad)
        self.saldo = saldo
        self.nacionalidad = self.validar_nacionalidad(nacionalidad)

    def validar_edad(self, edad):
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            return edad
        except ValueError:
            print("Error: La edad debe ser un número entero")
            return 0

    def validar_nacionalidad(self, nacionalidad):
        if nacionalidad.lower() != "peruana":
            print("Error: La nacionalidad debe ser peruana")
            return 'Peruana'
        return nacionalidad.capitalize()

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = self.validar_edad(input("Ingrese su edad: "))

    def cumpleaños(self):
        self.edad = self.edad + 1

def obtener_fecha_hora_minuto():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


persona1 = Persona("Max", 24, 1200, "Peruana")
persona2 = Persona("Elvis", 20, 1500, "Chilena")

#Datos
print("----- Datos de la persona 1 -----")
print("Nombre: {}\nEdad: {}\nSaldo: {}\nNacionalidad: {}"
      .format(persona1.nombre, persona1.edad, persona1.saldo, persona1.saldo, persona1.nacionalidad))

print("----- Datos de la persona 2 -----")
print("Nombre: {}\nEdad: {}\nSaldo: {}\nNacionalidad: {}"
      .format(persona2.nombre, persona2.edad, persona2.saldo, persona2.nacionalidad))

#Incrementamos edad
persona1.cumpleaños()
persona2.cumpleaños()


print("----- Edad actualizada después del cumpleaños -----")
print("Edad de la persona 1: {}".format(persona1.edad))
print("Edad de la persona 2: {}".format(persona2.edad))

print("Fecha, hora y minuto registrado: {}".format(obtener_fecha_hora_minuto()))
