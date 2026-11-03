# model/nodo_arbol.py

class NodoArbol:

    def __init__(self, centro):
        self.centro = centro
        self.izquierda = None
        self.derecha = None