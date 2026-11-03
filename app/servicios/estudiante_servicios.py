from dto.estudiante_dto import EstudianteDTO
from servicios.ordenador_estudiantes import OrdenadorEstudiantes


class EstudianteService:

    def __init__(self):
        self.estudiantes = []

    def crear_estudiante(
            self,
            codigo,
            nombre,
            edad):

        estudiante = EstudianteDTO(
            codigo,
            nombre,
            edad
        )

        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        return self.estudiantes

    def ordenar_bubble(self, criterio):

        return OrdenadorEstudiantes.bubble_sort(
            self.estudiantes,
            criterio
        )

    def ordenar_merge(self, criterio):

        return OrdenadorEstudiantes.merge_sort(
            self.estudiantes,
            criterio
        )