
from fastapi import APIRouter
from services.gerador_personagem import gerar_personagem

router = APIRouter()

@router.get("/")
def gerar():
    return gerar_personagem()
