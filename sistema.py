
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