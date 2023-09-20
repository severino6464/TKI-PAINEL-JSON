import subprocess
import time
import os

# Número total de salas
num_salas = 3

# Caminho para a pasta onde o código está sendo executado
base_path = os.path.dirname(os.path.abspath(__file__))

# Loop para executar os códigos de cada sala
for sala_numero in range(1, num_salas + 1):
    sala_codigo = f"sala{sala_numero}.py"
    subprocess.run(["python3", os.path.join(base_path, sala_codigo)])

# Intervalo de tempo em segundos após executar todas as salas
intervalo_no_final = 1  # por exemplo, 5 minutos

# Aguardar o intervalo de tempo após executar todas as salas
time.sleep(intervalo_no_final)
