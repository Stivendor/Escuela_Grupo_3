from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Tabla intermedia para la relación muchos a muchos entre materia y estudiante
materia_estudiante = Table(
    "materia_estudiante",
    Base.metadata,
    Column("materia_id", Integer, ForeignKey("materias.id"), primary_key=True),
    Column("estudiante_id", Integer, ForeignKey("estudiantes.id"), primary_key=True)
)

class Materia(Base):
    __tablename__ = "materias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(20), unique=True, nullable=False)

    # Relación con profesor (uno a muchos)
    profesor_id = Column(Integer, ForeignKey("profesores.id"))
    profesor = relationship("Profesor", backref="materias")

    # Relación con estudiantes (muchos a muchos)
    estudiantes = relationship(
        "Estudiante",
        secondary=materia_estudiante,
        backref="materias"
    )

    def __init__(self, nombre: str, codigo: str, profesor=None):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
        else:
            print(f"El estudiante {estudiante.nombre} ya está inscrito en {self.nombre}.")

    def listar_estudiantes(self):
        if not self.estudiantes:
            print(f"No hay estudiantes inscritos en {self.nombre}.")
        else:
            print(f"Estudiantes inscritos en {self.nombre}:")
            for estudiante in self.estudiantes:
                print(f"- {estudiante.nombre} (Matrícula: {estudiante.matricula})")