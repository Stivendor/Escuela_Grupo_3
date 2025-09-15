from sqlalchemy.orm import Session
from entities.persona import Persona

class PersonaCRUD:
    def create(self, db: Session, nombre: str, edad: int):
        persona = Persona(nombre=nombre, edad=edad)
        db.add(persona)
        db.commit()
        db.refresh(persona)
        return persona

    def get(self, db: Session, persona_id: int):
        return db.query(Persona).filter(Persona.id == persona_id).first()

    def get_all(self, db: Session):
        return db.query(Persona).all()

    def update(self, db: Session, persona_id: int, nombre: str = None, edad: int = None):
        persona = db.query(Persona).filter(Persona.id == persona_id).first()
        if persona:
            if nombre: persona.nombre = nombre
            if edad: persona.edad = edad
            db.commit()
            db.refresh(persona)
        return persona

    def delete(self, db: Session, persona_id: int):
        persona = db.query(Persona).filter(Persona.id == persona_id).first()
        if persona:
            db.delete(persona)
            db.commit()
        return persona
