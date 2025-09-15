from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base
from entities.persona import Persona

class Profesor(Persona):
    __tablename__ = "profesores"

    id = Column(Integer, ForeignKey("personas.id"), primary_key=True)
    especialidad = Column(String(50), nullable=False)