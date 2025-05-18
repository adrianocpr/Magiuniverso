# models.py
from pydantic import BaseModel

class Carteira(BaseModel):
    id_jogador: str
    saldo: float
    recursos: dict

class Propriedade(BaseModel):
    nome: str
    tipo: str
    dono: str
    valor: float

class Transacao(BaseModel):
    origem: str
    destino: str
    valor: float
    recurso: str
