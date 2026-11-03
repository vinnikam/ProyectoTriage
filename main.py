from servicios.estudiante_servicios import EstudianteService


def mostrar_estudiantes(estudiantes):

    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return

    print("\nLISTADO DE ESTUDIANTES")

    for estudiante in estudiantes:
        print(estudiante)


def solicitar_criterio():

    print("\nSeleccione criterio de ordenamiento")
    print("1. Nombre")
    print("2. Edad")

    opcion = input("Opción: ")

    if opcion == "1":
        return "nombre"

    return "edad"


def main():

    service = EstudianteService()

    while True:

        print("\n===================================")
        print(" SISTEMA DE ESTUDIANTES")
        print("===================================")
        print("1. Inscribir estudiante")
        print("2. Listar estudiantes")
        print("3. Ordenar Bubble Sort")
        print("4. Ordenar Merge Sort")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            try:
                codigo = int(input("Código: "))
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))

                service.crear_estudiante(
                    codigo,
                    nombre,
                    edad
                )

                print("\n✅ Estudiante registrado correctamente")

            except ValueError:
                print("\n❌ Datos inválidos")

        elif opcion == "2":

            mostrar_estudiantes(
                service.listar_estudiantes()
            )

        elif opcion == "3":

            criterio = solicitar_criterio()

            resultado = service.ordenar_bubble(
                criterio
            )

            print(
                f"\nESTUDIANTES ORDENADOS POR {criterio.upper()} (BUBBLE SORT)"
            )

            mostrar_estudiantes(resultado)

        elif opcion == "4":

            criterio = solicitar_criterio()

            resultado = service.ordenar_merge(
                criterio
            )

            print(
                f"\nESTUDIANTES ORDENADOS POR {criterio.upper()} (MERGE SORT)"
            )

            mostrar_estudiantes(resultado)

        elif opcion == "5":

            print("\nFinalizado...")
            break

        else:

            print("\n❌ Opción no válida")


if __name__ == "__main__":
    main()