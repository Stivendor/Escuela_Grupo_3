"""   OBJETIVOS:
    - Registrar estudiantes.
    - Mostrar lista de estudiantes.
"""
from models.estudiante import Estudiante

class GestionEstudiantes:
    def __init__(self):
        self.estudiantes = {}

    def registrar_estudiante(self, nombre, edad, matricula):
        estudiante = Estudiante(nombre, edad, matricula)
        self.estudiantes[matricula] = estudiante
        print(f"Estudiante {nombre} registrado con matrícula {matricula}.")

    def listar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        for estudiante in self.estudiantes.values():
            print(estudiante.presentarse())

    def obtener_estudiante(self, matricula):
        return self.estudiantes.get(matricula)