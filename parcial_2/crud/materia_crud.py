from sqlalchemy.orm import Session
from entities.materia import Materia

class MateriaCRUD:
    def create(self, db: Session, nombre: str, codigo: str, profesor_id: int):
        materia = Materia(nombre=nombre, codigo=codigo, profesor_id=profesor_id)
        db.add(materia)
        db.commit()
        db.refresh(materia)
        return materia

    def get(self, db: Session, materia_id: int):
        return db.query(Materia).filter(Materia.id == materia_id).first()

    def get_all(self, db: Session):
        return db.query(Materia).all()

    def update(self, db: Session, materia_id: int, nombre: str = None, codigo: str = None, profesor_id: int = None):
        materia = db.query(Materia).filter(Materia.id == materia_id).first()
        if materia:
            if nombre: materia.nombre = nombre
            if codigo: materia.codigo = codigo
            if profesor_id: materia.profesor_id = profesor_id
            db.commit()
            db.refresh(materia)
        return materia

    def delete(self, db: Session, materia_id: int):
        materia = db.query(Materia).filter(Materia.id == materia_id).first()
        if materia:
            db.delete(materia)
            db.commit()
        return materia
