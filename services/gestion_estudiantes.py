"""   OBJETIVOS:
    - Registrar estudiantes.
    - Mostrar lista de estudiantes.
"""
class GestionEstudiantes:
    def __init__(self): # Diccionario para almacenar estudiantes
        self.estudiantes = {}
    
    def registrar_estudiante(self, estudiante_id: str, nombre: str) -> str:
        """Registra un nuevo estudiante, evitando duplicados."""
        if estudiante_id in self.estudiantes:
            return f"El estudiante con ID '{estudiante_id}' ya está registrado."
        self.estudiantes[estudiante_id] = nombre
        return f"Estudiante '{nombre}' registrado exitosamente."
        
    def listar_estudiantes(self) -> str:
        """Muestra la lista de estudiantes registrados."""
        if not self.estudiantes: # Verifica si hay estudiantes registrados
            return "No hay estudiantes registrados."
        
        reporte = "Lista de estudiantes registrados: \n"
        for estudiante_id, nombre in self.estudiantes.items():
            reporte += f" ID: {estudiante_id} - Nombre: {nombre}\n"
        return reporte
# Ejemplo de uso
if __name__ == "__main__":
    gestion_estudiantes = GestionEstudiantes()
    print(gestion_estudiantes.registrar_estudiante("estudiante1", "Juan Perez"))
    print(gestion_estudiantes.registrar_estudiante("estudiante2", "Ana Gomez"))
    print(gestion_estudiantes.registrar_estudiante("estudiante1", "Pedro López"))  # Prueba duplicado
    print(gestion_estudiantes.listar_estudiantes())
