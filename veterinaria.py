class Propietarios:
    def __init__(self, nombre,telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Mascotas:
    def __init__(self, nombre, especie, raza, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.propietario = propietario


def Menu():
    print("--- Bienvenido a la Clínica Veterinaria ---")
    print("1. Registrar nuevo cliente")
    print("2. Registrar nueva mascota")
    print("3. Agendar cita médica")
    print("4. Ver historial de citas")
    print("5. Ver clientes y mascotas")
    print("0. Salir")

while True:
    Menu()
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                print("Registrar nuevo cliente")
            case 2:
                print("Registrar nueva mascota")
            case 3:
                print("Agendar Cita")
            case 4:
                print("Ver historial de citas")
            case 5:
                print("Ver clientes y mascotas")
            case 0:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion no valida")
    except ValueError:
        print("Debes ingresar un número")
