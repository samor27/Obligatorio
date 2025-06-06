import datetime
class Reposición:
    def __init__ (self, pieza, cantidad_lotes):
        self.__pieza= pieza
        self.__cantidad_lotes=(cantidad_lotes)
        self.__fecha=(datetime.date,datetime.time)
    
    @property
    def pieza(self):
        return self.__pieza
    
    @pieza.setter
    def pieza(self,pieza):
        self.__pieza = pieza

    @property
    def cantidad_lotes(self):
        return self.__cantidad_lotes
    
    @cantidad_lotes.setter
    def cantidad_lotes(self,cl):
        self.__cantidad_lotes = cl

    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self,co):
        self.__fecha = co
