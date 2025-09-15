from sqlalchemy.orm import Session
from entities.usuarios import Usuario

class UsuarioCRUD:
    def create(self, db: Session, username: str, password: str, rol: str):
        usuario = Usuario(username=username, password=password, rol=rol)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario

    def get(self, db: Session, user_id: int):
        return db.query(Usuario).filter(Usuario.id == user_id).first()

    def get_all(self, db: Session):
        return db.query(Usuario).all()

    def update(self, db: Session, user_id: int, username: str = None, password: str = None, rol: str = None):
        usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
        if usuario:
            if username:
                usuario.username = username
            if password:
                usuario.password = password
            if rol:
                usuario.rol = rol
            db.commit()
            db.refresh(usuario)
        return usuario

    def delete(self, db: Session, user_id: int):
        usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
        if usuario:
            db.delete(usuario)
            db.commit()
        return usuario
