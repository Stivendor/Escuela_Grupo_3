from sqlalchemy.orm import Session
from entities.periodo import Periodo

class PeriodoCRUD:
    def create(self, db: Session, nombre: str, fecha_inicio, fecha_fin):
        periodo = Periodo(nombre=nombre, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
        db.add(periodo)
        db.commit()
        db.refresh(periodo)
        return periodo

    def get(self, db: Session, periodo_id: int):
        return db.query(Periodo).filter(Periodo.id == periodo_id).first()

    def get_all(self, db: Session):
        return db.query(Periodo).all()

    def update(self, db: Session, periodo_id: int, nombre: str = None, fecha_inicio=None, fecha_fin=None):
        periodo = db.query(Periodo).filter(Periodo.id == periodo_id).first()
        if periodo:
            if nombre: periodo.nombre = nombre
            if fecha_inicio: periodo.fecha_inicio = fecha_inicio
            if fecha_fin: periodo.fecha_fin = fecha_fin
            db.commit()
            db.refresh(periodo)
        return periodo

    def delete(self, db: Session, periodo_id: int):
        periodo = db.query(Periodo).filter(Periodo.id == periodo_id).first()
        if periodo:
            db.delete(periodo)
            db.commit()
        return periodo
