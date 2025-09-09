"""   OBJETIVOS:
    - Registrar notas para un estudiante en una materia específica.
    - Calcular el promedio de notas para un estudiante.
    - Mostrar reportes de notas
"""
from models.estudiante import Estudiante

class GestionNotas:
    def registrar_nota(self, estudiante: Estudiante, materia: str, nota: float):
        estudiante.agregar_nota(materia, nota)
        print(f"Nota {nota} registrada para {estudiante.get_nombre()} en {materia}.")

    def calcular_promedio(self, estudiante: Estudiante):
        if not estudiante.notas:
            print(f"{estudiante.get_nombre()} no tiene notas registradas.")
            return 0
        
        print(f"\nNotas de {estudiante.get_nombre()}:")
        todas_las_notas = []
        for materia, lista_notas in estudiante.notas.items():
            notas_str = ", ".join(str(n) for n in lista_notas)
            print(f"- {materia}: {notas_str}")
            todas_las_notas.extend(lista_notas)

        promedio = sum(todas_las_notas) / len(todas_las_notas)
        print(f"\nEl promedio de {estudiante.get_nombre()} es {promedio:.2f}.")
        return promedio
