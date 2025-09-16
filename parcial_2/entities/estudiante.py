from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base
from entities.persona import Persona

class Estudiante(Persona):
    __tablename__ = "estudiantes"

    id = Column(Integer, ForeignKey("personas.id"), primary_key=True)
    matricula = Column(String(20), nullable=False)

    # Relación opcional si quieres que SQLAlchemy maneje la unión
    persona = relationship("Persona", backref="estudiante", uselist=False)
