from maquina import Maquina
from entities.pieza import Pieza
class Requerimiento:
    def __init__(self, maquina: Maquina, pieza, cantidad):
        self.maquina = maquina
        self.pieza = pieza
        self.cantidad = cantidad