from fastapi import FastAPI
from data import CONVENIOS, ORCAMENTOS, PREPAROS, EXAMES

app = FastAPI()

@app.get("/convenios")
def get_convenios()->list:
    convenios = CONVENIOS
    return convenios 

@app.get("/preparo/{exame_id}")
def get_preparo(exame_id:int)->list:
    response = [x for x in PREPAROS if x.get("id") == exame_id]
    return response

@app.get("/exames")
def get_exames()->list:
    exames = EXAMES
    return exames

@app.get("/orcamento/{exame_id}")
def get_orcamento(exame_id:int)->list:
    response = [x for x in ORCAMENTOS if x.get("id") == exame_id]
    return response