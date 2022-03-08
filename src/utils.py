from fastapi import HTTPException
from fastapi.openapi.utils import get_openapi

from decouple import config

SECRET_KEY = config("SECRET_KEY")

def get_api_key(api_key):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Não autorizado")
    else:
        pass

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema