from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base

class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)

    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=False)
    materia_id = Column(Integer, ForeignKey("materias.id"), nullable=False)

    # Relaciones
    estudiante = relationship("Estudiante", backref="notas")
    materia = relationship("Materia", backref="notas")