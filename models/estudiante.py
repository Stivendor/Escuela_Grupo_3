from .persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, matricula: str):
        super().__init__(nombre, edad) #llama al constructor de la clase Persona
        self.__matricula = matricula
        self.notas = {}
    
    def get_matricula(self):
        return self.__matricula

    def agregar_nota(self, materia: str, nota: float):
        self.notas[materia] = nota

    def presentarse(self):
        return f"Soy {self.get_nombre()}, estudiante con matricula {self.__matricula}."