
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

    def select_cliente(self):
        print ("Clientes: ") #Lista de clientes
        #for i in range (clientes):
            #print clientes[i]
        self.cliente = int(input("Introduzca el número de cliente"))

    def select_maquina(self):
        print("Maquinas: ") #Lista de Maquinas
        #for i in range (maquina):
            #print maquina[i]
        self.maquina = int(input("Introduzca el número de la maquina que quiera pedir: "))