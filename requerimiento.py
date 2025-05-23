from maquina import Maquina
from pieza import Pieza
class Requerimiento:
    def __init__(self, maquina: Maquina, pieza: Pieza, cantidad):
        self.maquina = maquina
        self.pieza = pieza
        self.cantidad = cantidad