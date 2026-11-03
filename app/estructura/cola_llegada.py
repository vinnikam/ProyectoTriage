from modelos.nodo import Nodo


class ColaLlegada:

    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, paciente):

        nuevo = Nodo(paciente)

        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo
            return

        self.final.siguiente = nuevo
        self.final = nuevo

    def desencolar(self):

        if self.frente is None:
            return None

        paciente = self.frente.dato
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        return paciente

    def ver_primero(self):
        return self.frente.dato if self.frente else None

    def listar(self):

        pacientes = []
        actual = self.frente

        while actual:
            pacientes.append(actual.dato)
            actual = actual.siguiente

        return pacientes

    def buscar(self, codigo):

        actual = self.frente

        while actual:

            if actual.dato.codigo == codigo:
                return actual.dato

            actual = actual.siguiente

        return None