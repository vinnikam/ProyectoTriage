# dto/centro_dto.py

class CentroDTO:

    def __init__(self, codigo, nombre, direccion):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.direccion}"