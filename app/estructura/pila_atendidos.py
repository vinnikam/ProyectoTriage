from modelos.nodo import Nodo


class PilaAtendidos:

    def __init__(self):
        self.tope = None

    def push(self, paciente):

        nuevo = Nodo(paciente)

        nuevo.siguiente = self.tope

        self.tope = nuevo

    def pop(self):

        if self.tope is None:
            return None

        paciente = self.tope.dato

        self.tope = self.tope.siguiente

        return paciente

    def peek(self):

        if self.tope:
            return self.tope.dato

        return None

    def listar_historial(self):

        historial = []
        actual = self.tope

        while actual:
            historial.append(actual.dato)
            actual = actual.siguiente

        return historial

    def buscar(self, codigo):

        actual = self.tope

        while actual:

            if actual.dato.codigo == codigo:
                return actual.dato

            actual = actual.siguiente

        return None