from enums.prioridad import Prioridad


class TriageService:

    def __init__(
            self,
            cola_llegada,
            lista_alta,
            lista_normal):

        self.cola_llegada = cola_llegada
        self.lista_alta = lista_alta
        self.lista_normal = lista_normal

    def clasificar_paciente(self, prioridad):

        paciente = self.cola_llegada.desencolar()

        if paciente is None:
            return None

        paciente.prioridad = prioridad

        if prioridad == Prioridad.ALTA:
            self.lista_alta.insertar_final(paciente)
        else:
            self.lista_normal.insertar_final(paciente)

        return paciente