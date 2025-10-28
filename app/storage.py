import json
from pathlib import Path

ARQUIVO = Path("senhas_criptografadas.json")

def salvar_dados(dados: dict):
    with ARQUIVO.open("w") as f:
        json.dump(dados, f, indent=4)

def ler_dados() -> dict:
    if not ARQUIVO.exists():
        return {}
    with ARQUIVO.open("r") as f:
        return json.load(f)
