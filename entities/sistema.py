from entities.pedido import Pedido
from entities.maquina import Maquina
from entities.cliente import Cliente
from entities.cliente import Empresa
from exceptions.cedula_invalida import CedulaInvalida
from exceptions.telefono_invalido import TelefonoInvalido
from entities.pieza import Pieza
import datetime 
from exceptions.cedula_invalida import CedulaInvalida
from exceptions.telefono_invalido import TelefonoInvalido
from exceptions.cliente_ya_existe import ClienteYaExiste
from exceptions.rut_invalido import Rut_invalido
from exceptions.correo_invalido import CorreoInvalido
from exceptions.pagina_invalida import PaginaInvalida

class Sistema:
  def __init__(self):
      self.clientes=[]
      self.piezas=[]
      self.maquinas=[]
      self.pedidos=[]
      self.max_clientes= 1
      self.codigo_pieza = 1
      self.codigo_maquina = 1
      self.costos = 0 
      self.ingresos = 0 
      self.pendiente = []

#Clientes
  
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
        nombre= Empresa(ID,telefono,correo,RUT,nombre,pagina_web)
        self.agregar_clientes(nombre)

  def registrar_particular(self, telefono,correo,cedula,nombre_completo):
        ID = self.max_clientes
        self.max_clientes+=1
        nombre_completo= Particular(ID,telefono,correo,cedula, nombre_completo)
        self.agregar_clientes(nombre_completo)

  def validar_cedula(self, ci):
     if len(str(ci))!=8:
        raise CedulaInvalida()
     if ci is str:
        raise TypeError
     
  def validar_telefono(self,tel):
     if len(str(tel))!=8:
        raise TelefonoInvalido
     if str(tel)[0]!="2":
        raise TelefonoInvalido
     
  def validar_empresa(self,nom):
      for i in range(len(self.clientes)):
         if self.clientes[i].nombre.lower().replace(" ","") == nom.lower().replace(" ",""):
            raise ClienteYaExiste 
  
  def validar_particular(self,nom):
       for i in range(len(self.clientes)):
          if self.clientes[i].nombre_completo.lower() == nom.lower():
             raise ClienteYaExiste
          
  def validar_rut(self, RUT):
     if len(str(RUT))!=12:
        raise Rut_invalido
   
  def validar_correo (self,correo):
     if "@" not in correo or "mail.com" not in correo:
        raise CorreoInvalido
  
  def validar_pagina(self,pagina):
     if ".com" not in pagina:
        raise PaginaInvalida

#REPONER
  
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
     repo = Reposición(pieza_a_reponer, cantidad_lotes)
     pieza.cantidad_disponible +=repo.cantidad_lotes
     print("Reposición realizada.")
     


#PIEZAS
  
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
  def registrar_pedido(self, cliente, maquina, fecha_entregado, estado, precio, piezas_faltantes):
      pedido = Pedido(cliente, maquina, fecha_entregado, estado, precio)
      self.pedidos.append(pedido)
      self.ingresos +=pedido.precio
      if estado == "pendiente":
         v=[pedido, piezas_faltantes]
         self.pendiente.append(v)
    
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
    piezas_faltantes = []
    for j in range(len(maquina.requerimientos)):
      pieza_cantidad = []
      if maquina.requerimientos[j].cantidad > maquina.requerimientos[j].pieza.cantidad_disponible:
        diferencia = (maquina.requerimientos[j].cantidad - maquina.requerimientos[j].pieza.cantidad_disponible)
        pieza_cantidad.append((maquina.requerimientos[j].pieza), (diferencia))
        piezas_faltantes.append(pieza_cantidad)
    if len(piezas_faltantes) == 0:
       return "entregado", piezas_faltantes
    else:
       maquina.requerimientos[j].pieza.cantidad_disponible -= maquina.requerimientos[j].cantidad
       return "pendiente", piezas_faltantes

  def fecha_entrega(estado):
     if estado == "pendiente":
        return "pendiente"
     else:
        return datetime.now()
     
  def pre (cliente, maquina):
    pre = (maquina.costo_produccion *1,5)
    if isinstance(cliente, Empresa):
      pre = pre*0,8
    return pre
     
  def listar_pedidos(self):
    if not self.pedidos:
      print("No hay pedidos registrados")
    else:
      print("Desesa filtrar los pedidos en 'Entregados' y 'Pendientes'?")
      filtro = input("si/no")
      while filtro != "si" or "no":
        print("Entrada no valida. Pruebe nuevamente:")
        print("Desesa filtrar los pedidos en 'Entregados' y 'Pendientes'?")
        filtro = input("si/no")
      if filtro == "si":
        entregados = []
        pendientes = []
        for i in range(len(self.pedidos)):
          if self.pedidos[i].estado == "entregado":
            entregados.append(self.pedidos[i])
          else:
            pendientes.append(self.pedidos[i])
        print("Entregados:")
        for j in range (len(entregados)):
          print(f"Cliente: [{entregados[j].cliente.ID}], Maquina: [{entregados[j].maquina.descripcion}], "
                f"Fecha recibido: [{entregados[j].fecha_recibido}], Fecha entregado: [{entregados[j].fecha_entregado}], "
                f"Estado: [{entregados[j].estado}], Precio: [{entregados[j].precio}]")
        print("Pendientes:")
        for k in range (len(pendientes)):
          print(f"Cliente: [{pendientes[k].cliente.ID}], Maquina: [{pendientes[k].maquina.descripcion}], "
                f"Fecha recibido: [{pendientes[k].fecha_recibido}], Fecha entregado: [{pendientes[k].fecha_entregado}], "
                f"Estado: [{pendientes[k]}], Precio: [{pendientes[k].precio}]")
      if filtro == "no":
         for l in range(self.pedidos):
            print(f"Cliente: [{self.pedidos[l].cliente.ID}], Maquina: [{self.pedidos[l].maquina.descripcion}], "
                 f"Fecha recibido: [{self.pedidos[l].fecha_recibido}], Fecha entregado: [{self.pedidos[l].fecha_entregado}], "
                 f"Estado: [{self.pedidos[l]}], Precio: [{self.pedidos[l].precio}]")
            

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


  def listar_maquinas (self):
    if not self.maquinas:
        print("No hay maquinas registradas")
    else: 
       for i in range(len(self.maquinas)):
          maquina = self.maquinas[i]
          print(f"Código: {maquina.codigo}, Descripción: {maquina.descripcion}, Costo: ${maquina.costo_produccion}")

#CONTABILIDAD

  def contabilidad (self):
   for i in range(len(self.pedidos)):
     if self.pedidos[i].estado == "entregado":
        self.costos += self.pedidos[i].maquina.costos_produccion
   print (("El costo total de las máquinas vendidadas es "), (self.costos))
   print  ("El total de ingresos es ", (self.ingresos))
   ganancias = self.ingresos - self.costos
   print ("La ganancia es ", ganancias) 
   gan_IRAE = ganancias*0.25
   gan_final=ganancias*0.75
   print ("El impuesto a las ganancias es de ", gan_IRAE)
   print ("La ganancia final es de ", gan_final)
   
