from .persona import Persona

class Estudiante:
    def __init__(self, matricula: str, nombre: str):
        self.__matricula = matricula
        self.__nombre = nombre
        self.notas = {}  # {materia: [lista de notas]}

    def get_matricula(self) -> str:
        return self.__matricula

    def get_nombre(self) -> str:
        return self.__nombre

    def agregar_nota(self, materia: str, nota: float):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)

    def calcular_promedio(self):
        total_notas = 0
        cantidad_notas = 0
        for notas_materia in self.notas.values():
            total_notas += sum(notas_materia)
            cantidad_notas += len(notas_materia)
        if cantidad_notas == 0:
            return None
        return total_notas / cantidad_notas

