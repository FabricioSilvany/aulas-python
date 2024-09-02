"""
Desenvolva um programa que conte quantos números negativos
foram inseridos pelo
usuário usando um laço while. 
O programa deve parar quando o usuário inserir 0 ou 
um número positivo. Mostre a quantidade de números negativos.
"""

import os
import time 

os.system("cls || clear")

#Declarando variáveis

contador = 0

#Solicitando dados

while True:
    numero = float(input("Digite um número negativo: "))
    contador += 1

    if numero >= 0:
        print(f"Quantidade de números inseridos: {contador}")
        break
