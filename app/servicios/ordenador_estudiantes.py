class OrdenadorEstudiantes:

    @staticmethod
    def obtener_valor(estudiante, criterio):
        if criterio == "nombre":
            return estudiante.nombre

        return estudiante.edad

    @staticmethod
    def bubble_sort(estudiantes, criterio):
        estudiantes = estudiantes.copy()
        n = len(estudiantes)
        for i in range(n):
            for j in range(0, n - i - 1):
                actual = OrdenadorEstudiantes.obtener_valor(
                    estudiantes[j],
                    criterio
                )
                siguiente = OrdenadorEstudiantes.obtener_valor(
                    estudiantes[j + 1],
                    criterio
                )

                if actual > siguiente:

                    estudiantes[j], estudiantes[j + 1] = (
                        estudiantes[j + 1],
                        estudiantes[j]
                    )
        return estudiantes

    @staticmethod
    def merge_sort(estudiantes, criterio):
        if len(estudiantes) <= 1:
            return estudiantes
        medio = len(estudiantes) // 2

        izquierda = OrdenadorEstudiantes.merge_sort(
            estudiantes[:medio],
            criterio
        )

        derecha = OrdenadorEstudiantes.merge_sort(
            estudiantes[medio:],
            criterio
        )

        return OrdenadorEstudiantes.merge(
            izquierda,
            derecha,
            criterio
        )

    @staticmethod
    def merge(izquierda, derecha, criterio):

        resultado = []

        i = 0
        j = 0

        while i < len(izquierda) and j < len(derecha):
            valor_izq = (
                OrdenadorEstudiantes.obtener_valor(
                    izquierda[i],
                    criterio
                )
            )
            valor_der = (
                OrdenadorEstudiantes.obtener_valor(
                    derecha[j],
                    criterio
                )
            )
            if valor_izq <= valor_der:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado