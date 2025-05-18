# services/economia_ia.py
import random

def simulador_economia(carteiras, transacoes):
    inflacao = random.uniform(-0.03, 0.05)
    for c in carteiras.values():
        c.saldo *= (1 + inflacao)
    return {"inflacao": inflacao, "carteiras": {k: c.dict() for k, c in carteiras.items()}}
