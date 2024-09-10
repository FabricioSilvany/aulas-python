"""
Crie um programa que leia 
3 notas, armazenadi em um vetor
e mostre as notas informadas.
"""

import os

os.system("cls || clear")

#Entrada
lista_notas = []

for i in range(3):
    notas = float(input(f"Digite a {i + 1}ª nota: "))
    lista_notas.append(notas)
    os.system("cls || clear")

#Saída
for i, nota in enumerate(lista_notas):
    print(f"{i + 1}ª nota: {nota}")