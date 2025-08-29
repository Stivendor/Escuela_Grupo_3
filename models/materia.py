from .profesor import Profesor
from .estudiante import Estudiante

class Materia:
    def __init__(self, nombre: str, codigo: str, profesor: Profesor = None):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__profesor = profesor
        self.__estudiantes = [] #lista de objetos de estudiante

    #getters y setters
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, nuevo_codigo: str):
        self.__codigo = nuevo_codigo

    def get_profesor(self):
        return self.__profesor
    
    def set_profesor(self, profesor: Profesor):
        self.__profesor = profesor

    def get_estudiantes(self):
        return self.__estudiantes
    
    #Metodos

    def agregar_estudiante(self, estudiante: Estudiante):
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)
        else:
            print(f"El estudiante {estudiante.get_nombre()} ya esta inscrito en {self.__nombre}.")
    
    def listar_estudiante(self):
        if not self.__estudiantes:
            print(f"No hay estudiantes inscritos en {self.__nombre}.")
        else:
            print(f"Estudiantes inscritos en {self.__nombre}:")
            for estudiante in self.__estudiantes:
                print(f"- {estudiante.get_nombre()} (Matricula: {estudiante.get_matricula()})")