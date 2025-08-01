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
    def registro(self):
        return f"Se asigno una mascota de Especie: {self.especie} Raza: {self.raza} Nombre: {self.nombre},Propietario: {self.propietario}"

class Perros(Mascotas):
    def __init__(self, nombre, raza, propietario):
        super().__init__(nombre, "Perro", raza, propietario)

    def registro(self):
        return f"Guaw! Se asigno un perro de Raza: {self.raza} Nombre: {self.nombre},Propietario: {self.propietario}"

class Gatos(Mascotas):
    def __init__(self, nombre, raza, propietario):
        super().__init__(nombre, "Gato", raza, propietario)

    def registro(self):
        return f"Miau! Se asigno un gato de Raza: {self.raza} Nombre: {self.nombre},Propietario: {self.propietario}"
class Peces(Mascotas):
    def __init__(self, nombre, raza, propietario):
        super().__init__(nombre, "Pez", raza, propietario)

    def registro(self):
        return f"Blub! Se asigno un pez de Raza: {self.raza} Nombre: {self.nombre},Propietario: {self.propietario}"

class Aves(Mascotas):
    def __init__(self, nombre, raza, propietario):
        super().__init__(nombre, "Ave", raza, propietario)

    def registro(self):
        return f"Pio! Se asigno un ave de Raza: {self.raza} Nombre: {self.nombre},Propietario: {self.propietario}"
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
                        if especie == "Perro":
                            nueva_mascota = Perros(nombre, raza, cliente.nombre)
                        elif especie == "Gato":
                            nueva_mascota = Gatos(nombre, raza, cliente.nombre)
                        elif especie == "Pez":
                            nueva_mascota = Peces(nombre, raza, cliente.nombre)
                        elif especie == "Ave":
                            nueva_mascota = Aves(nombre, raza, cliente.nombre)
                        mascotas.append(nueva_mascota)
                        print(nueva_mascota.registro())
                        break
                    else:
                        print("Propietario no encontrado")
            case 3:
                if not mascotas:
                    print("No hay mascotas registradas. Por favor, registra una mascota primero.")
                    continue
                print("Agendar cita médica")
                mascota_nombre = input("Ingresa nombre de la mascota: ")
                for mascota in mascotas:
                    if mascota.nombre == mascota_nombre:
                        fecha = input("Ingresa fecha de la cita (DD-MM-AAAA): ")
                        hora = input("Ingresa hora de la cita (HH:MM): ")
                        seleccion_motivo = int(input("Ingresa motivo de la cita (1.Enfermedad, 2.Requerida, 3.Operacion): "))
                        match seleccion_motivo:
                            case 1:
                                motivo = "Enfermedad"
                            case 2:
                                motivo = "Requerida"
                            case 3:
                                motivo = "Operacion"
                            case _:
                                print("Motivo no válido, por favor ingresa un número del 1 al 3")
                                break

                        nueva_cita = Citas(mascota, fecha, hora, motivo)
                        citas.append(nueva_cita)
                        print(f"Cita agendada para {mascota_nombre} el {fecha} a las {hora} por motivo: {motivo}")
                        print(nueva_cita.diagnostico())
                        break
                else:
                    print("Mascota no encontrada")
            case 4:
                print("Ver historial de citas")
                if not citas:
                    print("No hay citas registradas.")
                else:
                    for cita in citas:
                        print(f"Fecha: {cita.fecha}, Hora: {cita.hora}, Mascota: {cita.mascota.nombre}, Motivo: {cita.motivo}")
                        print(cita.diagnostico())
            case 5:
                print("Ver clientes y mascotas")
                if not clientes:
                    print("No hay clientes registrados.")
                else:
                    for cliente in clientes:
                        print(f"Cliente: {cliente.nombre}, Telefono: {cliente.telefono}, Correo: {cliente.correo}")
                        for mascota in mascotas:
                            if mascota.propietario == cliente.nombre:
                                print(f"  Mascota: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}")
            case 0:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion no valida")
    except ValueError:
        print("Debes ingresar un número")
