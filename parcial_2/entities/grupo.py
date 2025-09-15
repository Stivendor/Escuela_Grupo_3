from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

grupo_estudiante = Table(
    "grupo_estudiante",
    Base.metadata,
    Column("grupo_id", Integer, ForeignKey("grupos.id"), primary_key=True),
    Column("estudiante_id", Integer, ForeignKey("estudiantes.id"), primary_key=True)
)

class Grupo(Base):
    __tablename__ = "grupos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nulleable=False)

    materia_id = Column(Integer, ForeignKey("materias.id"), nulleable=False)
    profesor_id = Column(Integer, ForeignKey("profesores.id"), nulleable=False)

    #Relaciones
    materia = relationship("Materia", backref="grupos")
    profesor = relationship("Profesor", backref="grupos")
    estudiantes = relationship("Estudiante", secondary=grupo_estudiante, backref="grupos")