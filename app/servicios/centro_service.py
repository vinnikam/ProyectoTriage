# service/centro_service.py
from dto.centro_dto import CentroDTO
from modelos.arbol_centros import ArbolCentros
from modelos.grafo import Grafo


class CentroService:

    def __init__(self):

        self.arbol = ArbolCentros()
        self.grafo = Grafo()

        self.centros = {}

    def crear_centro(
            self,
            codigo,
            nombre,
            direccion):

        centro = CentroDTO(
            codigo,
            nombre,
            direccion
        )

        self.centros[codigo] = centro

        self.arbol.insertar(
            centro
        )

        self.grafo.agregar_centro(
            centro
        )

    def registrar_recorrido(
            self,
            codigo_origen,
            codigo_destino,
            kilometros):

        origen = self.centros.get(
            codigo_origen
        )

        destino = self.centros.get(
            codigo_destino
        )

        if origen and destino:

            self.grafo.agregar_recorrido(
                origen,
                destino,
                kilometros
            )

    def listar_centros(self):

        return self.arbol.listar_ordenados()

    def listar_recorridos(
            self,
            codigo):

        return self.grafo.obtener_recorridos(
            codigo
        )