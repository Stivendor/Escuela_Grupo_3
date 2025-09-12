from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Periodo(Base):
    __tablename__= "periodos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)

    #Relacion con grupo (un periodo puede tener muchos grupos)
    grupos = relationship("Grupo", backref="periodo")