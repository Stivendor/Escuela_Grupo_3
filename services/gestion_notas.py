"""   OBJETIVOS:
    - Registrar notas para un estudiante en una materia específica.
    - Calcular el promedio de notas para un estudiante.
    - Mostrar reportes de notas
"""
class GestionNotas:
    def __init__(self):
        self.notas = {}  # Diccionario para almacenar notas por estudiante y materia

    def registrar_nota(self, estudiante_id: str, materia: str, nota: float) -> None:
        """Registra una nota para un estudiante en una materia específica."""
        self.notas.setdefault(estudiante_id, {}).setdefault(materia, []).append(nota)

    def calcular_promedio(self, estudiante_id: str) -> float:
        """Calcula el promedio de notas para un estudiante."""
        materias = self.notas.get(estudiante_id, {})
        total_notas = sum(sum(notas) for notas in materias.values())
        cantidad_notas = sum(len(notas) for notas in materias.values())
        return total_notas / cantidad_notas if cantidad_notas > 0 else 0.0

    def mostrar_reporte(self, estudiante_id: str) -> str:
        """Muestra un reporte de notas para un estudiante."""
        if estudiante_id not in self.notas:
            return "No hay notas registradas para este estudiante."
        reporte = f"Reporte de notas para el estudiante {estudiante_id}:\n"
        for materia, notas in self.notas[estudiante_id].items():
            promedio_materia = sum(notas) / len(notas) if notas else 0.0
            reporte += f" Materia: {materia} - Notas: {notas} - Promedio: {promedio_materia:.2f}\n"
        promedio_general = self.calcular_promedio(estudiante_id)
        reporte += f"Promedio General: {promedio_general:.2f}\n"
        return reporte

# Ejemplo de uso
if __name__ == "__main__":
    gestion_notas = GestionNotas()
    gestion_notas.registrar_nota("estudiante1", "Matemáticas", 5)
    gestion_notas.registrar_nota("estudiante2", "Matemáticas", 4)
    gestion_notas.registrar_nota("estudiante1", "Historia", 2)
    gestion_notas.registrar_nota("estudiante1", "Historia", 5)

    print(gestion_notas.mostrar_reporte("estudiante1"))
    print(gestion_notas.mostrar_reporte("estudiante2"))




