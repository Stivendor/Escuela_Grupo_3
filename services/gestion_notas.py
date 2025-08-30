"""   OBJETIVOS:
    - Registrar notas para un estudiante en una materia específica.
    - Calcular el promedio de notas para un estudiante.
    - Mostrar reportes de notas
"""
from models.estudiante import Estudiante
from models.materia import Materia

class GestionNotas:
    def __init__(self):
        self.materias = {}  # clave: código materia, valor: objeto Materia

    def registrar_materia(self, nombre: str, codigo: str, profesor=None):
        if codigo in self.materias:
            print(f"Ya existe una materia con código {codigo}.")
            return
        materia = Materia(nombre, codigo, profesor)
        self.materias[codigo] = materia
        print(f"Materia {nombre} registrada con código {codigo}.")

    def inscribir_estudiante(self, codigo: str, estudiante: Estudiante):
        materia = self.materias.get(codigo)
        if materia:
            materia.agregar_estudiante(estudiante)
            print(f"Estudiante {estudiante.get_nombre()} inscrito en {materia.get_nombre()}.")
        else:
            print(f"No existe la materia con código {codigo}.")

    def registrar_nota(self, estudiante: Estudiante, materia: str, nota: float):
        estudiante.agregar_nota(materia, nota)
        print(f"Nota {nota} registrada para {estudiante.get_nombre()} en {materia}.")

    def calcular_promedio(self, estudiante: Estudiante):
        if not estudiante.notas:
            print(f"{estudiante.get_nombre()} no tiene notas registradas.")
            return 0
        promedio = sum(estudiante.notas.values()) / len(estudiante.notas)
        print(f"El promedio de {estudiante.get_nombre()} es {promedio:.2f}.")
        return promedio

    def reporte_estudiante(self, estudiante: Estudiante):
        if not estudiante.notas:
            print(f"{estudiante.get_nombre()} no tiene notas registradas.")
            return
        print(f"Notas de {estudiante.get_nombre()}:")
        for materia, nota in estudiante.notas.items():
            print(f"- {materia}: {nota}")
