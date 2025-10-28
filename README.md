# Gerenciador de Senhas

Um protótipo de gerenciador de senhas feito com **FastAPI** e **Python** com interface em HTML. Permite salvar as senhas localmente e gerar senhas aleatórias.

## Funcionalidades atuais

- Salvar senhas localmente
- Gerar senhas aleatórias
- Interface web com formulário para inserção e visualização de senhas
- Armazenamento local das senhas.
- Importação de senhas via CSV.
- Exportação de senhas para CSV.

> Nota: Este é apenas um protótipo. Criptografia e armazenamento seguro ainda não foram implementados.

## Tecnologias

- Python 3.x
- FastAPI
- Jinja2 (templates HTML)
- Uvicorn (servidor local)

## Como rodar localmente

1. Clone o repositório:
   
git clone https://github.com/joao1815/gerenciador_senhas.git
cd gerenciador_senhas

2. criar e ativar um ambiente virtual

**python -m venv venv**
**source venv/bin/activate (no Linux/macOS)**

**venv\Scripts\activate  ( no Windows)**

4. instalar as dependencias

**pip install -r requirements.txt**

6. rode o servidor localmente

**uvicorn app.main:app --reload**

7. acessar no navegador

**http://127.0.0.1:8000**
