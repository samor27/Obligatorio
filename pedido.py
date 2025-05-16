
import datetime
class Pedido:
    def __init__(self, cliente, maquina, fecha_entregado, estado):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recibido = datetime.date
        self.fecha_entregado = fecha_entregado
        self.estado = estado #pendiente o entregado
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio (self, pre):
        self.__precio = pre

class Sistema:
  def __init__(self,max_clientes,clientes,piezas,maquinas,pedido):
      self.clientes=[]
      self.piezas=[]
      self.maquinas=[]
      self.pedidos=[]
      self.__max_clientes=0
  @property
  def max_clientes(self):
    return self.__max_clientes
  @max_clientes.setter
  def max_clientes(self,num):
    self.__max_clientes=num
  def aumentar_clientes():
    max_clientes +=1