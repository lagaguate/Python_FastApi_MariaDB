"""
Pasos para montar la instancia
1. Activar Conda entorno virtual
> conda activate fast-api
2. Activar Docker
> sudo docker ps -a
> sudo docker start mysql
3. Ejecutar uvicorn para Fastapi
> uvicorn app:app --reload
"""

from fastapi import FastAPI
from routers.user import user

app = FastAPI(
    title="Ejercicio #1 Fast-Api",
    description="Ejemplo CRUD con FAST-API",
    version="0.0.5",
    openapi_tags=[{
        "name": "users",
        "description": "Router users"
    }])

app.include_router(user)
