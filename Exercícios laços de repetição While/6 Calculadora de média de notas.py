"""
Crie um programa que ajude um estudante
a calcular a média de suas notas.
O programa deve permitir que o usuário insira
notas de provas até que o usuário insira um valor negativo.
O programa deve calcular e exibir a média das notas inseridas.
"""

import os 
os.system("cls || clear")

#Declaração de variáveis

soma = 0
contador = 0

#Solicitando dados
while True:
    notas = float(input("Digite uma nota: "))
        
    if notas < 0:
        break

    soma += notas
    contador += 1

media = soma / contador
print(f"Média {media}")






