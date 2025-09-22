from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, essa é a minha primeira API com python"}

@app.get("/saudacao/{nome}")
def saudar(nome: str):
    return{"mensagem": f'Ola, {nome}, bem vindo a API'}