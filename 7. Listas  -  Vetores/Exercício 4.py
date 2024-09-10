"""
Crie um programa que leia 5 números, armazenando
em um vetor e informe qual é o menor e o maior.

Mostre os números informados pelo usuário
"""

import os

os.system("cls || clear")

#Entrada
lista_numeros = []

for i in range(5):
    numeros = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numeros)
    os.system("cls || clear")

#Processamento
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

#Saída
print("====RESULTADOS====")
for i, numero in enumerate(lista_numeros):
    print(f"{i + 1}º número: {numero}")

print(f"\nMaior número: {maior_numero}")
print(f"Menor número: {menor_numero}")