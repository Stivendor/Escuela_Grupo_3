"""   OBJETIVOS:
    - Registrar notas para un estudiante en una materia específica.
    - Calcular el promedio de notas para un estudiante.
    - Mostrar reportes de notas
"""
class GestionNotas:
    def __init__(self, gestion_estudiantes):
        self.gestion_estudiantes = gestion_estudiantes

    def registrar_nota(self, matricula, materia, nota):
        estudiante = self.gestion_estudiantes.obtener_estudiante(matricula)
        if estudiante:
            estudiante.agregar_nota(materia, nota)
            print(f"Nota registrada para {estudiante.get_nombre()} en {materia}: {nota}")
        else:
            print("Estudiante no encontrado.")

    def mostrar_reporte(self):
        for estudiante in self.gestion_estudiantes.estudiantes.values():
            print(f"Notas de {estudiante.get_nombre()} ({estudiante.get_matricula()}):")
            if estudiante.notas:
                for materia, nota in estudiante.notas.items():
                    print(f"  {materia}: {nota}")
            else:
                print("  Sin notas registradas.")



