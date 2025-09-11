from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from entities.persona import Persona

class Profesor(Persona):
    __tablename__ = "profesores"

    id = Column(Integer, ForeignKey("personas.id"), primary_key=True)
    especialidad = Column(String(50), nullable=False)

    persona = relationship("Persona", backref="profesor", uselist=False)

    def __init__(self, nombre: str, edad: int, especialidad: str):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def presentarse(self):
        return f"Soy {self.nombre}, profesor de {self.especialidad}."