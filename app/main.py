# Comentarios en español: API que recibe una cédula y consulta al backend-data
from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

BACKEND_DATA_URL = os.getenv('BACKEND_DATA_URL', 'http://backend-data:8081')

@app.get('/person/{cedula}')
async def get_person(cedula: str):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{BACKEND_DATA_URL}/person/{cedula}", timeout=5.0)
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
