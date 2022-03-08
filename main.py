from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from src.data import CONVENIOS, ORCAMENTOS, PREPAROS, EXAMES
from src.utils import get_api_key,custom_openapi

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


app.openapi_schema =  get_openapi(
        title="Lumia Get Started",
        version="0.0.1",
        description="Api para simulação de integração com a Lumia",
        routes=app.routes,
)