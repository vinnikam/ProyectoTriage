class AtencionService:

    def __init__(
            self,
            lista_alta,
            lista_normal,
            historial):

        self.lista_alta = lista_alta
        self.lista_normal = lista_normal
        self.historial = historial

    def atender_paciente(self):

        if not self.lista_alta.esta_vacia():
            paciente = self.lista_alta.eliminar_primero()

        else:
            paciente = self.lista_normal.eliminar_primero()

        if paciente:
            self.historial.push(paciente)

        return paciente