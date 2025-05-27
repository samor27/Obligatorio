from entities.pedido import Pedido
from entities.maquina import Maquina
from entities.cliente import Cliente
from entities.requerimiento import Requerimiento
import datetime 
class Sistema:
  def __init__(self):
      self.clientes=[]
      self.piezas=[]
      self.maquinas=[]
      self.pedidos=[]
      self.__max_clientes= 1
      self.codigo_pieza = 1
  
  @property
  def max_clientes(self):
    return self.__max_clientes
  @max_clientes.setter
  def max_clientes(self,num):
    self.__max_clientes=num
  def aumentar_clientes():
    max_clientes +=1

  def registrar_pieza(self,descripcion,costo,tamaño_lote,cantidad_disponible):
    for i in range(len(self.piezas)):
          if self.piezas[i].descripcion.lower() == descripcion.lower():
             raise ValueError("La pieza ya está registrada")
    codigo = self.codigo_pieza
    nueva_pieza = Pieza(codigo, descripcion, costo, tamaño_lote,cantidad_disponible)
    self.piezas.append(nueva_pieza)  
    self.codigo_pieza += 1

  def buscar_pieza_por_codigo(self,codigo):
    for i in range (len(self.piezas)):
        if self.piezas[i].codigo == codigo:
            return self.piezas[i]
    raise ValueError("Pieza no encontrada")
  
  def reponer_pieza(self,codigo,cantidad_lotes):
    pieza = self.buscar_pieza_por_codigo(codigo)
    cantidad_a_agregar = cantidad_lotes * pieza.tamaño_lote
    pieza.agregar_stock(cantidad_a_agregar)

    
  def listar_piezas(self):
    if not self.piezas:
      print("No hay piezas registradas")
    else:
      for i in range(len(self.piezas)):
        pieza = self.piezas[i]
        print(f"Código: {pieza.codigo}, Descripción: {pieza.descripcion}, Costo: {pieza.costo}, Tamaño de lote: {pieza.tamaño_lote}, Cantidad disponible: {pieza.cantidad_disponible}")

  
  #Pedido
  def registrar_pedido(self, cliente, maquina, fecha_entregado, estado):
      cliente = Pedido(cliente, maquina, fecha_entregado, estado)
      self.pedidos.append(cliente)

  
  def select_cliente(self):
      print ("Clientes: ") #Lista de clientes
      for i in range (len(self.clientes)):
        Cliente = self.clientes[i]
        print (f"{i}) {Cliente.ID}")

      cond = False
      while cond == False:
          num = int(input("Introduzca el número de cliente"))
          for i in range (self.clientes):
              if num == i:
                cliente = self.clientes[i]
                return cliente
          print("El numero ingresado no corresponde con ningun cliente." /
              "Pruebe de nuevo")


  def select_maquina(self):
      print("Maquinas: ") #Lista de Maquinas
      for i in range (self.maquinas):
        Maquina = self.maquina[i]
        print (f"{i}) {Maquina.descripcion}")

      cond = False
      while cond == False:
        num = int(input("Introduzca el número de la maquina que quiera pedir: "))
        for i in range (maquina):
          if num == i:
            maquina = maquina[i]
            return maquina
        else:
          print("El numero ingresado no corresponde con ninguna Maquina." /
          "Pruebe de nuevo")

    
  def entrega(self, maquina):
    m = [Requerimiento.cantidad ]
      if stock[i][1] == 
        if stock[j] >= Requerimiento.cantidad:
          self.estado = "entregado"
          self.fecha_entregado = (datetime.date, datetime.time)
        else:
          self.estado = "pendiente"
          self.fecha_entregado = "pendiente"