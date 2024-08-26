import os
import time
os.system("cls || clear")

#Declarando variáveis

#Solicitando dados
numero = int(input(f"\nDigite um número: "))

for i in range(numero, 0 , -1):
    print(f"Número: {i}")
    time.sleep(1)


