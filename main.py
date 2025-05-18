
from fastapi import FastAPI
from api.routes.planeta import router as planeta_router
from api.routes.personagem import router as personagem_router

app = FastAPI()

app.include_router(planeta_router, prefix="/gerar_planeta", tags=["Planeta"])
app.include_router(personagem_router, prefix="/gerar_personagem", tags=["Personagem"])
