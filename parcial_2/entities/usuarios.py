from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    rol = Column(String(20), nullable=False)

    #un usuario puede estar asociado a un estudiante o un profesor
    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=True)
    profesor_id = Column(Integer, ForeignKey("profesores.id"), nullable=True)

    estudiante = relationship("Estudiante", backref="usuario", uselist=False)
    profesor = relationship("Profesor", backref="usuario", uselist=False)