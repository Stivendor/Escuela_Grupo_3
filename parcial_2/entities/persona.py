from sqlalchemy import Column, Integer, String
from database import Base

class Persona(Base):
    __tablename__ = "personas"  # Nombre de la tabla en la BD

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)