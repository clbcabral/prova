from fastapi import FastAPI

app = FastAPI()

@app.get('/{id_obj}')
def get(id_obj, q = None):
    print(id_obj, q)
    return {1,3,4}