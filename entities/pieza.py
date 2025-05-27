class Pieza:
    def __init__(self,codigo,descripcion,costo,tamaño_lote,cantidad_disponible):
        self.codigo = codigo
        self.descripcion = descripcion
        self.costo = costo
        self.tamaño_lote = tamaño_lote
        self.cantidad_disponible = cantidad_disponible
    
    def agregar_stock(self,cantidad):
        self.cantidad_disponible += cantidad

    def quitar_stock(self,cantidad):
        if cantidad > self.cantidad_disponible:
            raise ValueError("No hay suficiente stock disponible")
        self.cantidad_disponible -= cantidad   


   

