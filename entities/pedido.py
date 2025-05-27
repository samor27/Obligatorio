from entities.cliente import Cliente
from entities.maquina import Maquina
import datetime
#import costo_de_produccion from Maquina
class Pedido:
    def __init__(self, cliente: Cliente, maquina: Maquina, fecha_entregado, estado):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recibido = datetime.now()
        self.fecha_entregado = fecha_entregado
        self.estado = estado #pendiente o entregado
        self.__precio = 0
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio (self, costo_produccion):
        pre = (costo_produccion + (costo_produccion*0.5))
        # if self.cliente == Empresa:
        #     self.__precio = pre*0,8
        # else:
        #     self.__precio = pre







                  
      