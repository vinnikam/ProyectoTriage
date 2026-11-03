from dataclasses import dataclass
from app.enums.prioridad import Prioridad


@dataclass
class PacienteDTO:
    codigo: str
    nombre_completo: str
    edad: int
    prioridad: Prioridad | None = None

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre_completo} | "
            f"Edad: {self.edad} | "
            f"Prioridad: {self.prioridad.value if self.prioridad else 'SIN ASIGNAR'}"
        )