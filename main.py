from fastapi import FastAPI
from db import Base, engine
from models import user

app = FastAPI()

# Criação das tabelas
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API com PostgreSQL conectada com sucesso"}
