from abc import ABC

from modelos.nodo import Nodo


class ListaEspera(ABC):

    def __init__(self):
        self.cabeza = None

    def insertar_final(self, paciente):

        nuevo = Nodo(paciente)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def eliminar_primero(self):

        if self.cabeza is None:
            return None

        paciente = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente

        return paciente

    def listar(self):

        pacientes = []
        actual = self.cabeza

        while actual:
            pacientes.append(actual.dato)
            actual = actual.siguiente

        return pacientes

    def buscar(self, codigo):

        actual = self.cabeza

        while actual:

            if actual.dato.codigo == codigo:
                return actual.dato

            actual = actual.siguiente

        return None

    def esta_vacia(self):
        return self.cabeza is None