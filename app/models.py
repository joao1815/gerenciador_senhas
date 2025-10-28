from sqlalchemy import Column, Integer, String
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)

class Senha(Base):
    __tablename__ = "senhas"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    dados = Column(String, nullable=False)
    nonce = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    usuario_id = Column(Integer, nullable=False)  
