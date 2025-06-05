from entities.pedido import Pedido
from entities.maquina import Maquina
from entities.cliente import Cliente
from entities.requerimiento import Requerimiento
from exceptions.cedula_invalida import CedulaInvalida
from exceptions.telefono_invalido import TelefonoInvalido
from entities.pieza import Pieza
import datetime 
class Sistema:
  def __init__(self):
      self.clientes=[]
      self.piezas=[]
      self.maquinas=[]
      self.pedidos=[]
      self.max_clientes= 1
      self.codigo_pieza = 1
      self.codigo_maquina = 1
  def agregar_clientes(self,cliente: Cliente):
    self.clientes.append(cliente)

  def listar_emp(self):
    for i in range (0,len(self.clientes)):
       Empresa= self.clientes[i]
       if len(vars(Empresa)) == 6:
        print (f"ID: {Empresa.ID}, Teléfono: {Empresa.telefono}, Correo: {Empresa.correo}, RUT: {Empresa.RUT}, Nombre: {Empresa.nombre}, Página web: {Empresa.pagina_web}")

  def listar_par(self):
     for i in range (0,len(self.clientes)):
        Particular = self.clientes [i]
        if len(vars(Particular)) == 5:
          print (f"ID: {Particular.ID}, Teléfono: {Particular.telefono}, Correo: {Particular.correo}, Cédula: {Particular.cedula}, Nombre: {Particular.nombre_completo}")

  def registrar_empresa(self,telefono,correo,RUT,nombre,pagina_web):
        ID=self.max_clientes
        self.max_clientes +=1
        nombre=Empresa(ID,telefono,correo,RUT,nombre,pagina_web)
        self.agregar_clientes(nombre)

  def registrar_particular(self, telefono,correo,cedula,nombre_completo):
        ID = self.max_clientes
        self.max_clientes+=1
        nombre_completo=Particular(ID,telefono,correo,cedula, nombre_completo)
        self.agregar_clientes(nombre_completo)
 
  def validar_cedula(self, ci):
     if len(str(ci))!=8:
        raise CedulaInvalida()
     if ci is str:
        raise TypeError
  def validar_telefono(self,tel):
     if len(str(tel))!=8:
        raise TelefonoInvalido

  def reponer (self):
     for i in range (len(self.piezas)):
        p=self.piezas[i]
        print(f"Código: {p.codigo}, Descripción: {p.descripcion}")
     codigo = int(input ("Ingrese el código de la píeza a reponer "))
     pieza_a_reponer = None
     for pieza in self.piezas:
        if pieza.codigo == codigo:
            pieza_a_reponer = pieza
            break

     if pieza_a_reponer is None:
        print("Pieza no encontrada.")
        return
     cantidad_lotes = int(input("Ingrese la cantidad a reponer: "))
     repo= Reposición(pieza_a_reponer, cantidad_lotes)
     pieza.cantidad_disponible +=repo.cantidad_lotes
     print("Reposición realizada.")

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
    return None
  
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
    for j in range(len(maquina.requerimientos)):
      if maquina.requerimientos[j].cantidad <= maquina.requerimientos[j].pieza.cantidad_disponible:

#Maquina

  def registrar_maquina(self,descripcion,codigos_piezas,cantidades):
    for i in range(len(self.maquinas)):
        if self.maquinas[i].descripcion.lower() == descripcion.lower():
          raise Exception("Ya existe una maquina con esa descripcion")
        
      
    nueva_maquina = Maquina(self.codigo_maquina,descripcion)
    
    for i in range(len(codigos_piezas)):
      codigo = codigos_piezas[i]
      cantidad = cantidades[i]

      pieza = self.buscar_pieza_por_codigo(codigo)

      if pieza is not None:
          nueva_maquina.nuevo_requerimiento(pieza,cantidad)
      else:
         print("La pieza con el codigo",codigo,"no fue encontrada.")

    nueva_maquina.calcular_costo_produccion()
    self.maquinas.append(nueva_maquina)
    self.codigo_maquina += 1


  def listar_maquinas(self):
    if not self.maquinas:
        print("No hay maquinas registradas")
    else: 
       for i in range(len(self.maquinas)):
          maquina = self.maquinas[i]
          print(f"Código: {maquina.codigo}, Descripción: {maquina.descripcion}, Costo: ${maquina.costo_produccion}")
          
