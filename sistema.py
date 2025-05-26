
class Sistema:
  def __init__(self,max_clientes,clientes,piezas,maquinas,pedido):
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

        
