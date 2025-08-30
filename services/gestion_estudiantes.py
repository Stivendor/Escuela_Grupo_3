"""   OBJETIVOS:
    - Registrar estudiantes.
    - Mostrar lista de estudiantes.
"""
from models.estudiante import Estudiante

class GestionEstudiantes:
    def __init__(self):
        self.estudiantes = {}

    def registrar_estudiante(self, nombre: str, edad: int, matricula: str):
        if matricula in self.estudiantes:
            print(f"Ya existe un estudiante con matrícula {matricula}.")
            return
        estudiante = Estudiante(nombre, edad, matricula)
        self.estudiantes[matricula] = estudiante
        print(f"Estudiante {nombre} registrado con matrícula {matricula}.")

    def listar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        print("Listado de estudiantes:")
        for estudiante in self.estudiantes.values():
            print(estudiante.presentarse())

    def obtener_estudiante(self, matricula: str):
        return self.estudiantes.get(matricula)