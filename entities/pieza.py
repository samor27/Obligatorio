class Pieza:
    def __init__(self,codigo,descripcion,costo,tamaño_lote):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__costo = costo
        self.__tamaño_lote = tamaño_lote
        self.__cantidad_disponible = 0

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

    @property
    def costo(self):
        return self.__costo
    
    @costo.setter
    def costo(self,costo):
        self.__costo = costo

    @property
    def tamaño_lote(self):
        return self.__tamaño_lote
    
    @tamaño_lote.setter
    def tamaño_lote(self,tamaño_lote):
        self.tamaño_lote = tamaño_lote

    @property
    def cantidad_disponible(self):
        return self.__cantidad_disponible
    
    @cantidad_disponible.setter
    def cantidad_disponible(self,cantidad_disponible):
        self.cantidad_disponible = cantidad_disponible

   
    
   

   

