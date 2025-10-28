from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)

def criar_usuario(db: Session, username: str, senha: str):
    senha_hash = hash_senha(senha)
    usuario = models.Usuario(username=username, senha_hash=senha_hash)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def autenticar_usuario(db: Session, username: str, senha: str):
    usuario = db.query(models.Usuario).filter(models.Usuario.username == username).first()
    if not usuario:
        return None
    if not verificar_senha(senha, usuario.senha_hash):
        return None
    return usuario
