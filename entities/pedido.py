from entities.cliente import Cliente
from entities.maquina import Maquina
from datetime import datetime
class Pedido:
    def __init__(self, cliente: Cliente, maquina: Maquina, fecha_entregado, estado, precio):
        self.__cliente = cliente
        self.__maquina = maquina
        self.__fecha_recibido = datetime.now()
        self.__fecha_entregado = fecha_entregado
        self.__estado = estado
        self.precio = precio

    
    @property
    def cliente (self):
        return self.__cliente
    
    @cliente.setter
    def cliente (self, cliente):
        self.__cliente = cliente


    @property
    def maquina(self):
        return self.__maquina
    
    @maquina.setter
    def maquina (self, maquina):
        self.__maquina = maquina


    @property
    def fecha_recibido(self):
        return self.__fecha_recibido
    

    @property
    def fecha_entregado(self):
        return self.__fecha_entregado
    
    @fecha_entregado.setter
    def fecha_entregado(self, fecha_entregado):
        self.__fecha_entregado = fecha_entregado


    @property
    def estado (self):
        return self.__estado
    
    @estado.setter
    def estado (self, estado):
        self.__estado = estado










                  
      