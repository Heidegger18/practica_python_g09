
"""
2. Usando el concepto de herencia y encapsulación (para saldo) para crear
elsiguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas.
"""

class Persona:
    def __init__(self, nombre, edad, saldo, nacionalidad):
        self.nombre = nombre
        self.edad = self.validar_edad(edad)
        self.__saldo = saldo  #Encapsulamiento del saldo
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
            return "Peruana"
        return nacionalidad.capitalize()

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = self.validar_edad(input("Ingrese su edad: "))

    def cumpleaños(self):
        self.edad = self.edad + 1

    def transferencia(self, persona_destino, monto):
        if self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            persona_destino.__saldo = persona_destino.__saldo + monto
            print("Transferencia de {} realizada con éxito".format(monto))
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        return self.__saldo  # Método para acceder al saldo encapsulado


# Crear dos instancias de la clase Persona
persona1 = Persona("Max", 24, 1200, "Peruana")
persona2 = Persona("Elvis", 20, 1400, "Chilena")

print("---- INICIO DE LOS SALDOS ----")
print("Saldo de {}: {}".format(persona1.nombre, persona1.mostrar_saldo()))
print("Saldo de {}: {}".format(persona2.nombre, persona2.mostrar_saldo()))

print("---- TRANSFERENCIA ----")
persona1.transferencia(persona2, 290)

print("---- SALDOS ACTUALIZADOS ----")
print(f"Saldo de {persona1.nombre}: {persona1.mostrar_saldo()}")
print(f"Saldo de {persona2.nombre}: {persona2.mostrar_saldo()}")

print("---- TRANSFERENCIA ----")
persona2.transferencia(persona1, 2000)
