from fastapi import FastAPI, HTTPException
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

def get_api_key(api_key):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Não autorizado")
    else:
        pass