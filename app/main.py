from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gerenciador de Senhas Seguro",
    description="API para gerar, armazenar e criptografar senhas com AES-GCM.",
    version="1.0.0"
)

app.include_router(router)
