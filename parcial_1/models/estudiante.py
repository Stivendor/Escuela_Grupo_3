from .persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, matricula: str):
        super().__init__(nombre, edad)
        self.__matricula = matricula
        self.notas = {}  # {materia: [lista de notas]}
    
    def get_matricula(self):
        return self.__matricula

    # Agregar una nota para una materia específica
    def agregar_nota(self, materia: str, nota: float):
        lista_notas = self.notas.get(materia, [])
        lista_notas.append(nota)
        self.notas[materia] = lista_notas


    def presentarse(self):
        return f"Soy {self.get_nombre()}, estudiante con matrícula {self.__matricula}."
