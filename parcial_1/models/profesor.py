from .persona import Persona

class Profesor(Persona):
    def __init__(self, nombre: str, edad: int, especialidad: str):
        super().__init__(nombre, edad)
        self.__especialidad = especialidad
    
    def get_especialidad(self):
        return self.__especialidad
    
    def presentarse(self):
        return f"Soy {self.get_nombre()}, profesor de {self.__especialidad}."