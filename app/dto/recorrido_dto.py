# dto/recorrido_dto.py

class RecorridoDTO:

    def __init__(self, origen, destino, kilometros):
        self.origen = origen
        self.destino = destino
        self.kilometros = kilometros

    def __str__(self):
        return (
            f"{self.origen.nombre} -> "
            f"{self.destino.nombre} "
            f"({self.kilometros} Km)"
        )