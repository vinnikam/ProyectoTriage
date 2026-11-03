class EstudianteDTO:

    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return (
            f"Codigo: {self.codigo} "
            f"Nombre: {self.nombre} "
            f"Edad: {self.edad}"
        )