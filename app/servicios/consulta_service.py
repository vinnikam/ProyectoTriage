class ConsultaService:

    def __init__(
            self,
            cola_llegada,
            lista_alta,
            lista_normal,
            historial):

        self.cola_llegada = cola_llegada
        self.lista_alta = lista_alta
        self.lista_normal = lista_normal
        self.historial = historial

    def ver_llegadas(self):
        return self.cola_llegada.listar()

    def ver_lista_espera(self):

        return {
            "alta": self.lista_alta.listar(),
            "normal": self.lista_normal.listar()
        }

    def ver_historial(self):
        return self.historial.listar_historial()

    def buscar_paciente(self, codigo):

        paciente = self.cola_llegada.buscar(codigo)

        if paciente:
            return paciente, "COLA DE LLEGADA"

        paciente = self.lista_alta.buscar(codigo)

        if paciente:
            return paciente, "ALTA PRIORIDAD"

        paciente = self.lista_normal.buscar(codigo)

        if paciente:
            return paciente, "PRIORIDAD NORMAL"

        paciente = self.historial.buscar(codigo)

        if paciente:
            return paciente, "ATENDIDOS"

        return None, "NO ENCONTRADO"