from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, telefono, correo):
        self.ID=0
        self.telefono=telefono 
        self.correo=correo 
class Particular(Cliente):
    def __init__(self,ID,telefono,correo,cedula,nombre_completo):
        self.cedula=cedula
        self.nombre_completo=nombre_completo
        super().__init__(ID,telefono,correo)
class Empresa(Cliente):
    def __init__(self,ID,telefono,correo,RUT,nombre,pagina_web):
        super().__init__(ID,telefono,correo,)
        self.RUT=RUT
        self.nombre=nombre
        self.pagina_web=pagina_web
