from sqlalchemy import Column, Integer, String
from database import Base

class Persona(Base):
    __tablename__ = "personas"  # Nombre de la tabla en la BD

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre}, y tengo {self.edad}."