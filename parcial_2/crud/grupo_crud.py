from sqlalchemy.orm import Session
from entities.grupo import Grupo

class GrupoCRUD:
    def create(self, db: Session, nombre: str, materia_id: int, profesor_id: int, periodo_id: int):
        grupo = Grupo(nombre=nombre, materia_id=materia_id, profesor_id=profesor_id, periodo_id=periodo_id)
        db.add(grupo)
        db.commit()
        db.refresh(grupo)
        return grupo

    def get(self, db: Session, grupo_id: int):
        return db.query(Grupo).filter(Grupo.id == grupo_id).first()

    def get_all(self, db: Session):
        return db.query(Grupo).all()

    def update(self, db: Session, grupo_id: int, nombre: str = None, materia_id: int = None, profesor_id: int = None, periodo_id: int = None):
        grupo = db.query(Grupo).filter(Grupo.id == grupo_id).first()
        if grupo:
            if nombre: grupo.nombre = nombre
            if materia_id: grupo.materia_id = materia_id
            if profesor_id: grupo.profesor_id = profesor_id
            if periodo_id: grupo.periodo_id = periodo_id
            db.commit()
            db.refresh(grupo)
        return grupo

    def delete(self, db: Session, grupo_id: int):
        grupo = db.query(Grupo).filter(Grupo.id == grupo_id).first()
        if grupo:
            db.delete(grupo)
            db.commit()
        return grupo
