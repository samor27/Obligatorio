from .requerimiento import Requerimiento
class Maquina:
    def __init__(self,codigo,descripcion):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.requerimientos = []
        self.costo_produccion = 0
        

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self,descripcion):
        self.__descripcion = descripcion    
    
    

    def nuevo_requerimiento(self,pieza,cantidad):
        nuevo_req = Requerimiento(pieza,cantidad)
        self.requerimientos.append(nuevo_req)

    def calcular_costo_produccion(self):
        self.costo_produccion = 0
        for i in range(len(self.requerimientos)):
            pieza = self.requerimientos[i].pieza
            cantidad = self.requerimientos[i].cantidad
            self.costo_produccion += pieza.costo * cantidad
