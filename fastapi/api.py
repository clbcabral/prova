from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/{id_obj}')
def get(id_obj, q = None):
    print(id_obj, q)
    return {1,3,4}

## Para rodar: uvicorn api:app