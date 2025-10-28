from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import string, secrets, base64

from .database import get_db
from . import crypto, models, auth
from .schemas import UsuarioCreate, UsuarioLogin

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "titulo": "Gerador de Senhas"})

@router.get("/senhas/")
async def gerar_senhas():
    caracteres = string.ascii_letters + string.digits + "!@#%&*"
    senha = ''.join(secrets.choice(caracteres) for _ in range(12))
    return {"senha": senha}

@router.post("/register/")
def register(user: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.Usuario).filter(models.Usuario.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    novo = auth.criar_usuario(db, user.username, user.senha)
    return {"id": novo.id, "username": novo.username}

@router.post("/login/")
def login(user: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = auth.autenticar_usuario(db, user.username, user.senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
    return {"id": usuario.id, "username": usuario.username, "msg": "Login realizado com sucesso"}

@router.post("/salvar-senha/{usuario_id}")
def salvar_senha(usuario_id: int, label: str, dados: str, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    salt = crypto.gerar_salt()
    chave = crypto.gerar_chave("senha_mestra", salt) 
    resultado = crypto.criptografar(dados, chave)

    nova_senha = models.Senha(
        label=label,
        dados=resultado["dados"],
        nonce=resultado["nonce"],
        salt=base64.b64encode(salt).decode(),
        usuario_id=usuario.id
    )
    db.add(nova_senha)
    db.commit()
    db.refresh(nova_senha)

    return {"id": nova_senha.id, "label": nova_senha.label}
