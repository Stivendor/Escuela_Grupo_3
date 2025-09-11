from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from entities.persona import Persona

class Estudiante(Persona):
    __tablename__ = "estudiantes"

    id = Column(Integer, ForeignKey("personas.id"), primary_key=True)
    matricula = Column(String(20), nullable=False)

    # Relación opcional si quieres que SQLAlchemy maneje la unión
    persona = relationship("Persona", backref="estudiante", uselist=False)

    def __init__(self, nombre: str, edad: int, matricula: str):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.notas = {}  #esto es un diccionario en memoria, no se guarda en la BD

    def agregar_nota(self, materia: str, nota: float):
        self.notas[materia] = nota

    def presentarse(self):
        return f"Soy {self.nombre}, estudiante con matrícula {self.matricula}."