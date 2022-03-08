from fastapi import FastAPI, HTTPException
from data import CONVENIOS, ORCAMENTOS, PREPAROS, EXAMES
from utils import get_api_key

app = FastAPI()

@app.get("/convenios")
def get_convenios(api_key:str=None)->list:
    get_api_key(api_key)
    convenios = CONVENIOS
    return convenios 
    
@app.get("/preparo/{exame_id}")
def get_preparo(exame_id:int,api_key:str=None)->list:
    get_api_key(api_key)
    response = [x for x in PREPAROS if x.get("id") == exame_id]
    if not response:
        raise HTTPException(status_code=404, detail="Exame não localizado")
    return response

@app.get("/exames")
def get_exames(api_key:str=None)->list:
    get_api_key(api_key)
    exames = EXAMES
    return exames

@app.get("/orcamento/{exame_id}")
def get_orcamento(exame_id:int,api_key:str=None)->list:
    get_api_key(api_key)
    response = [x for x in ORCAMENTOS if x.get("id") == exame_id]
    if not response:
        raise HTTPException(status_code=404, detail="Exame não localizado")
    return response