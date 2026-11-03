# model/grafo.py

from dto.recorrido_dto import RecorridoDTO


class Grafo:

    def __init__(self):
        self.adyacencias = {}

    def agregar_centro(self, centro):

        if centro.codigo not in self.adyacencias:
            self.adyacencias[centro.codigo] = []

    def agregar_recorrido(
            self,
            origen,
            destino,
            kilometros):

        recorrido = RecorridoDTO(
            origen,
            destino,
            kilometros
        )

        self.adyacencias[origen.codigo].append(
            recorrido
        )

    def obtener_recorridos(
            self,
            codigo_centro):

        return self.adyacencias.get(
            codigo_centro,
            []
        )