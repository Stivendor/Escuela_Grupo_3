from sqlalchemy.orm import Session
from entities.nota import Nota

class NotaCRUD:
    def create(self, db: Session, valor: float, estudiante_id: int, materia_id: int):
        nota = Nota(valor=valor, estudiante_id=estudiante_id, materia_id=materia_id)
        db.add(nota)
        db.commit()
        db.refresh(nota)
        return nota

    def get(self, db: Session, nota_id: int):
        return db.query(Nota).filter(Nota.id == nota_id).first()

    def get_all(self, db: Session):
        return db.query(Nota).all()

    def update(self, db: Session, nota_id: int, valor: float = None):
        nota = db.query(Nota).filter(Nota.id == nota_id).first()
        if nota:
            if valor: nota.valor = valor
            db.commit()
            db.refresh(nota)
        return nota

    def delete(self, db: Session, nota_id: int):
        nota = db.query(Nota).filter(Nota.id == nota_id).first()
        if nota:
            db.delete(nota)
            db.commit()
        return nota
