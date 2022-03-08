from fastapi import FastAPI, HTTPException
from decouple import config

SECRET_KEY = config("SECRET_KEY")

def get_api_key(api_key):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Não autorizado")
    else:
        pass