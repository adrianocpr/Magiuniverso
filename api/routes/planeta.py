
from fastapi import APIRouter
from services.gerador_planeta import gerar_planeta

router = APIRouter()

@router.get("/")
def gerar():
    return gerar_planeta()
