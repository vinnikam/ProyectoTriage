# model/arbol_centros.py
from modelos.nodo_arbol import NodoArbol


class ArbolCentros:

    def __init__(self):
        self.raiz = None

    def insertar(self, centro):
        self.raiz = self.__insertar(self.raiz, centro)

    def __insertar(self, nodo, centro):

        if nodo is None:
            return NodoArbol(centro)

        if centro.nombre < nodo.centro.nombre:
            nodo.izquierda = self.__insertar(
                nodo.izquierda,
                centro
            )
        else:
            nodo.derecha = self.__insertar(
                nodo.derecha,
                centro
            )

        return nodo

    def listar_ordenados(self):

        resultado = []

        self.__inorden(
            self.raiz,
            resultado
        )

        return resultado

    def __inorden(self, nodo, lista):

        if nodo is None:
            return

        self.__inorden(nodo.izquierda, lista)

        lista.append(nodo.centro)

        self.__inorden(nodo.derecha, lista)