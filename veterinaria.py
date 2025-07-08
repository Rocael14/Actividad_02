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

class Citas:
    def __init__(self, mascota, fecha, hora, motivo):
        self.mascota = mascota
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

    def diagnostico(self):
        if self.motivo == "Enfermedad":
            return "Diagnóstico: Requiere atención veterinaria inmediata"
        elif self.motivo == "Requerida":
            return "Diagnóstico: Revisión general y vacunación"
        elif self.motivo == "Operacion":
            return "Diagnóstico: Requiere cirugía programada"
        else:
            return "Diagnóstico: Motivo no reconocido"


def Menu():
    print("--- Bienvenido a la Clínica Veterinaria ---")
    print("1. Registrar nuevo cliente")
    print("2. Registrar nueva mascota")
    print("3. Agendar cita médica")
    print("4. Ver historial de citas")
    print("5. Ver clientes y mascotas")
    print("0. Salir")

clientes = []
mascotas = []
citas = []
while True:
    Menu()
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                print("Registrar nuevo cliente")
                nombre = input("Ingresa nombre de cliente: ").capitalize()
                telefono = input("Ingresa telefono de cliente: ")
                correo = input("Ingresa correo de cliente: ")
                clientes.append(Propietarios(nombre, telefono, correo))
                print(f"Cliente {nombre} registrado exitosamente")
            case 2:
                if not clientes:
                    print("No hay clientes registrados. Por favor, registra un cliente primero.")
                    continue
                print("Registrar nueva mascota")
                propietario = input("Ingresa el correo del propietario: ")
                for cliente in clientes:
                    if cliente.correo == propietario:
                        nombre = input("Ingresa nombre de la mascota: ")
                        seleccion_especie = int(input("Ingresa especie de la mascota(1.Perros, 2.Gatos, 3.Peces y 4.Aves): "))
                        match seleccion_especie:
                                case 1:
                                    especie = "Perro"
                                case 2:
                                    especie = "Gato"
                                case 3:
                                    especie = "Pez"
                                case 4:
                                    especie = "Ave"
                                case _:
                                    print("Especie no válida, por favor ingresa un número del 1 al 4")
                                    break
                        raza = input("Ingresa raza de la mascota: ")
                        mascotas.append(Mascotas(nombre, especie, raza, cliente.nombre))
                        print(f"Mascota {nombre} registrada exitosamente al propietario {cliente.nombre}")
                        break
                    else:
                        print("Propietario no encontrado")
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
