from .persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, matricula: str):
        super().__init__(nombre, edad)
        self.__matricula = matricula
        self.notas = {}  # {materia: [lista de notas]}
    
    def get_matricula(self):
        return self.__matricula

    def agregar_nota(self, materia: str, nota: float):
        returns = self.notas.get(materia, [])
        returns.append(nota)
        self.notas[materia] = returns

    def presentarse(self):
        return f"Soy {self.get_nombre()}, estudiante con matrícula {self.__matricula}."
