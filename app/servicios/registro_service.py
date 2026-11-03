from app.dto.paciente_dto import PacienteDTO


class RegistroService:

    def __init__(self, cola_llegada):
        self.cola_llegada = cola_llegada
        self.consecutivo = 1

    def registrar_paciente(self, nombre, edad):

        codigo = f"P{self.consecutivo:04d}"

        paciente = PacienteDTO(
            codigo=codigo,
            nombre_completo=nombre,
            edad=edad
        )

        self.cola_llegada.encolar(paciente)

        self.consecutivo += 1

        return paciente