from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, ID, telefono, correo):
        self.__telefono=telefono
        self.__ID=ID 
        self.__correo=correo 
    @property
    def telefono (self):
        return self.__telefono

    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono

    @property
    def ID (self):
        return self.__ID

    @ID.setter
    def ID(self,id):
        self.__ID=id

    @property
    def correo (self):
        return self.__correo

    @correo.setter
    def correo(self,correo):
        self.__correo=correo

class Particular(Cliente):
    def __init__(self,ID, telefono,correo,cedula,nombre_completo):
        self.__cedula=cedula
        self.__nombre_completo=nombre_completo
        super().__init__(ID,telefono,correo)
    @property
    def cedula (self):
        return self.__cedula

    @cedula.setter
    def cedula(self,cedula):
        self.__cedula=cedula
    
    @property
    def nombre_completo (self):
        return self.__nombre_completo

    @nombre_completo.setter
    def nombre_completo(self,nomcompleto):
        self.__nombre_completo=nomcompleto

class Empresa(Cliente):
    def __init__(self, ID, telefono,correo,RUT,nombre,pagina_web):
        super().__init__(ID,telefono,correo)
        self.__RUT=RUT
        self.__nombre=nombre
        self.__pagina_web=pagina_web
    
    @property
    def RUT (self):
        return self.__RUT

    @RUT.setter
    def RUT(self,RUT):
        self.__RUT=RUT

    @property
    def nombre (self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def pagina_web (self):
        return self.__pagina_web

    @pagina_web.setter
    def pagina_web(self,pagina_web):
        self.__pagina_web=pagina_web
