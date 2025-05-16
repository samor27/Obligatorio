class Sistema:
  def__init__(self,max_clientes,clientes,piezas,maquinas,pedido):
    self.clientes=[]
    self.piezas=[]
    self.maquinas=[]
    self.pedidos=[]
    self.__max_clientes=0
  @Property
  def max_clientes(self):
    return self.__max_clientes
  @max_clientes.setter
  def max_clientes(self,num):
    self.__max_clientes=num
    
