from fastapi import HTTPException
from fastapi.openapi.utils import get_openapi

from decouple import config

SECRET_KEY = config("SECRET_KEY")

def get_api_key(api_key):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Não autorizado")
    else:
        pass
