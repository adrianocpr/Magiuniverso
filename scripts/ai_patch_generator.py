# Simula uma IA que edita um arquivo de código
import os

file_path = "app/main.py"

# Simula uma sugestão de melhoria no código
if os.path.exists(file_path):
    with open(file_path, "a") as f:
        f.write("\n# Sugestão automática da IA: adicionar logging futuramente\n")
else:
    os.makedirs("app", exist_ok=True)
    with open(file_path, "w") as f:
        f.write("# Arquivo criado pela IA\nprint('Olá, mundo IA!')\n")