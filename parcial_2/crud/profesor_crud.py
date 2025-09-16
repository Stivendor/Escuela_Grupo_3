from sqlalchemy.orm import Session
from entities.profesor import Profesor

class ProfesorCRUD:
    def create(self, db: Session, nombre: str, edad: int, especialidad: str):
        profesor = Profesor(nombre=nombre, edad=edad, especialidad=especialidad)
        db.add(profesor)
        db.commit()
        db.refresh(profesor)
        return profesor

    def get(self, db: Session, profesor_id: int):
        return db.query(Profesor).filter(Profesor.id == profesor_id).first()

    def get_all(self, db: Session):
        return db.query(Profesor).all()

    def update(self, db: Session, profesor_id: int, nombre: str = None, edad: int = None, especialidad: str = None):
        profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()
        if profesor:
            if nombre: profesor.nombre = nombre
            if edad: profesor.edad = edad
            if especialidad: profesor.especialidad = especialidad
            db.commit()
            db.refresh(profesor)
        return profesor

    def delete(self, db: Session, profesor_id: int):
        profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()
        if profesor:
            db.delete(profesor)
            db.commit()
        return profesor
