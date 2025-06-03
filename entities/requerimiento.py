from entities.pieza import Pieza
class Requerimiento:
    def __init__(self,pieza:Pieza,cantidad):
        self.__pieza = pieza
        self.__cantidad = cantidad
    @property
    def pieza(self):
        return self.__pieza
    @pieza.setter
    def pieza(self,pieza):
        self.__pieza = pieza
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad
