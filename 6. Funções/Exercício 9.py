"""
Escreva um programa que permita ler 3
notas de um aluno, usando laço de repetição 
e informe por meio de uma função a média.
"""

import os
os.system("cls || clear")

notas = 0

def calcular_media(notas):
    soma = notas
    media = soma / 3
    return media

#Entrada
for i in range(3):
    notas += int(input(f"Digite a {i + 1}ª nota: "))

#Processamento
media = calcular_media(notas)

#Saida
print(f"Média: {media:.1f}")
