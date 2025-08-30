from models.estudiante import Estudiante

class Materia:
    def __init__(self, codigo: str, nombre: str):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__estudiantes = []

    def get_codigo(self) -> str:
        return self.__codigo

    def get_nombre(self) -> str:
        return self.__nombre

    def agregar_estudiante(self, estudiante: Estudiante):
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)
        else:
            print(f"El estudiante {estudiante.get_nombre()} ya está inscrito en {self.__nombre}.")

    def listar_estudiantes(self):
        if not self.__estudiantes:
            print(f"No hay estudiantes inscritos en {self.__nombre}.")
        else:
            print(f"Estudiantes inscritos en {self.__nombre}:")
            for estudiante in self.__estudiantes:
                print(f"- {estudiante.get_nombre()} (Matrícula: {estudiante.get_matricula()})")
