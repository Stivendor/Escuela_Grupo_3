from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.config import Base

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