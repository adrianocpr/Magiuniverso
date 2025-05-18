
import random

def gerar_planeta():
    tipos = ["Terrestre", "Gasoso", "Gélido", "Vulcânico"]
    biomas = ["Floresta", "Deserto", "Ártico", "Oceânico"]
    return {
        "nome": f"Planeta-{random.randint(1000, 9999)}",
        "tipo": random.choice(tipos),
        "bioma_dominante": random.choice(biomas),
        "habitável": random.choice([True, False]),
    }
