
import datetime
#import costo_de_produccion from Maquina
class Pedido:
    def __init__(self, cliente, maquina, fecha_entregado, estado):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recibido = (datetime.date, datetime.time)
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

    def select_cliente():
        print ("Clientes: ") #Lista de clientes
        #for i in range (clientes):
            #print (i, clientes[i])
        cond = False
        while cond == False:
            num = int(input("Introduzca el número de cliente"))
            # for i in range (clientes):
            #     if num == i:
            #         cliente = clientes[i]
            #         cond = True
            #     else:
            #         print("El numero ingresado no corresponde con ningun cliente./
            #          Pruebe de nuevo")
            #return cliente


    def select_maquina():
        print("Maquinas: ") #Lista de Maquinas
        #for i in range (maquina):
            #print (i, maquina[i])
        cond = False
        while cond == False:
            num = int(input("Introduzca el número de la maquina que quiera pedir: "))
            # for i in range (maquina):
            #     if num == i:
            #         maquina = maquina[i]
            #         cond = True
            #     else:
            #         print("El numero ingresado no corresponde con ninguna Maquina./
            #          Pruebe de nuevo")
        #return maquina
    
    def entrega(self, stock, piezas_maquina):
        #if stock[j] == piezas_maquina:
            #self.estado = "entregado"
            #self.fecha_entregado = (datetime.date, datetime.time)
        #else:
            #self.estado = "pendiente"
            #self.fecha_entregado = "pendiente"