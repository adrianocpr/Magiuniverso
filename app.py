from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Servidor rodando com sucesso na Render!"}