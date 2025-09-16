from sqlalchemy.orm import Session
from entities.estudiante import Estudiante

class EstudianteCRUD:
    def create(self, db: Session, nombre: str, edad: int, matricula: str):
        estudiante = Estudiante(nombre=nombre, edad=edad, matricula=matricula)
        db.add(estudiante)
        db.commit()
        db.refresh(estudiante)
        return estudiante

    def get(self, db: Session, estudiante_id: int):
        return db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()

    def get_all(self, db: Session):
        return db.query(Estudiante).all()

    def update(self, db: Session, estudiante_id: int, nombre: str = None, edad: int = None, matricula: str = None):
        estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
        if estudiante:
            if nombre: estudiante.nombre = nombre
            if edad: estudiante.edad = edad
            if matricula: estudiante.matricula = matricula
            db.commit()
            db.refresh(estudiante)
        return estudiante

    def delete(self, db: Session, estudiante_id: int):
        estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
        if estudiante:
            db.delete(estudiante)
            db.commit()
        return estudiante
