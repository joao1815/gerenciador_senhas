from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
import os
import base64

def gerar_salt() -> bytes:
    return os.urandom(16)

def gerar_chave(senha: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    return kdf.derive(senha.encode())

def criptografar(dados: str, chave: bytes) -> dict:
    aesgcm = AESGCM(chave)
    nonce = os.urandom(12)
    dados_criptografados = aesgcm.encrypt(nonce, dados.encode(), None)
    return {
        "nonce": base64.b64encode(nonce).decode(),
        "dados": base64.b64encode(dados_criptografados).decode()
    }

def descriptografar(dados: str, nonce: str, chave: bytes) -> str:
    aesgcm = AESGCM(chave)
    dados = base64.b64decode(dados)
    nonce = base64.b64decode(nonce)
    return aesgcm.decrypt(nonce, dados, None).decode()
