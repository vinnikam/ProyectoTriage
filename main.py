from facade.hospital_facade import HospitalFacade
from enums.prioridad import Prioridad


def mostrar_pacientes(lista):

    if not lista:
        print("\nNo hay pacientes.")
        return

    for paciente in lista:
        print(paciente)


def menu():
    print("\n" + "=" * 50)
    print(" SISTEMA DE GESTIÓN HOSPITALARIA ")
    print("=" * 50)
    print("1. Registrar paciente")
    print("2. Clasificar paciente (Triage)")
    print("3. Atender paciente")
    print("4. Ver cola de llegada")
    print("5. Ver lista de espera")
    print("6. Ver historial de atendidos")
    print("7. Buscar paciente")
    print("0. Salir")
    print("=" * 50)


def main():

    hospital = HospitalFacade()

    while True:

        menu()

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":

                nombre = input("Nombre completo: ")
                edad = int(input("Edad: "))

                paciente = hospital.registro.registrar_paciente(
                    nombre,
                    edad
                )

                print("\nPaciente registrado correctamente")
                print(paciente)

            case "2":

                siguiente = hospital.consulta.cola_llegada.ver_primero()

                if not siguiente:
                    print("\nNo hay pacientes pendientes de clasificación.")
                    continue

                print("\nPaciente a clasificar:")
                print(siguiente)

                print("\n1. ALTA")
                print("2. NORMAL")

                opcion_prioridad = input(
                    "Seleccione prioridad: "
                )

                if opcion_prioridad == "1":
                    prioridad = Prioridad.ALTA
                else:
                    prioridad = Prioridad.NORMAL

                paciente = hospital.triage.clasificar_paciente(
                    prioridad
                )

                print("\nPaciente clasificado:")
                print(paciente)

            case "3":

                paciente = hospital.atencion.atender_paciente()

                if paciente:
                    print("\nPaciente atendido:")
                    print(paciente)
                else:
                    print("\nNo hay pacientes en espera.")

            case "4":

                print("\nCOLA DE LLEGADA")
                mostrar_pacientes(
                    hospital.consulta.ver_llegadas()
                )

            case "5":

                espera = hospital.consulta.ver_lista_espera()

                print("\nALTA PRIORIDAD")
                mostrar_pacientes(espera["alta"])

                print("\nPRIORIDAD NORMAL")
                mostrar_pacientes(espera["normal"])

            case "6":

                print("\nHISTORIAL DE ATENDIDOS")

                mostrar_pacientes(
                    hospital.consulta.ver_historial()
                )

            case "7":

                codigo = input(
                    "Ingrese código del paciente: "
                ).upper()

                paciente, ubicacion = (
                    hospital.consulta.buscar_paciente(
                        codigo
                    )
                )

                if paciente:
                    print("\nPaciente encontrado")
                    print(paciente)
                    print(f"Ubicación: {ubicacion}")
                else:
                    print("\nPaciente no encontrado.")

            case "0":

                print("\nGracias por usar el sistema.")
                break

            case _:

                print("\nOpción inválida.")


if __name__ == "__main__":
    main()