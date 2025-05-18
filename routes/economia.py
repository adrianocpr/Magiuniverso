# routes/economia.py
from fastapi import APIRouter
from models import Carteira, Propriedade, Transacao
from services.economia_ia import simulador_economia

router = APIRouter()

carteiras = {}
propriedades = {}
transacoes = []

@router.post("/carteira")
def criar_carteira(dados: Carteira):
    carteiras[dados.id_jogador] = dados
    return {"status": "carteira criada"}

@router.post("/propriedade")
def registrar_propriedade(dados: Propriedade):
    propriedades[dados.nome] = dados
    return {"status": "propriedade registrada"}

@router.post("/transacao")
def realizar_transacao(dados: Transacao):
    transacoes.append(dados)
    return {"status": "transação realizada"}

@router.get("/simular")
def simular_economia():
    return simulador_economia(carteiras, transacoes)
