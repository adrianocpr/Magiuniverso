
import random

def gerar_personagem():
    raças = ["Humano", "Elfo", "Orc", "Ciborgue"]
    classes = ["Guerreiro", "Mago", "Engenheiro", "Mercador"]
    personalidades = ["Leal", "Caótico", "Neutro", "Benevolente"]
    return {
        "nome": f"Personagem-{random.randint(1000, 9999)}",
        "raça": random.choice(raças),
        "classe": random.choice(classes),
        "personalidade": random.choice(personalidades),
        "nível": random.randint(1, 10)
    }
