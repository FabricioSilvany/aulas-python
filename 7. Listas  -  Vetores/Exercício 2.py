"""
Crie um programa que leia 3 notas, armazenando
em vetor e calcule a média aritimética.

Mostre as 3 notas informadas pelo usuário e informe a média.
"""

import os

os.system("cls || clear")

#Declaração de variáveis e constantes
soma = 0
QUANTIDADE_NOTAS = 3
#Entrada
lista_notas = []

for i in range(3):
    notas = float(input(f"Digite a {i + 1}ª nota: "))
    lista_notas.append(notas)
    os.system("cls || clear")

#Processamento
soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

#Saída
for i, nota in enumerate(lista_notas):
    print(f"{i + 1}ª nota: {notas}")

print(f"\nMédia: {media}")

