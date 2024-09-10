"""
Crie um programa que leia 6 números,
armazenando em um vetor e informe quantos são
pares e quantos são ímpares

Mostre os números informados pelo usuário.
"""

import os

os.system("cls || clear")


#Entrada
lista_numeros = []

impares = 0
pares = 0

for i in range(6):
    numeros = int(input(f"Digite o {i+1} número: "))
    lista_numeros.append(numeros)
    os.system("cls || clear")
    
#Processamento
    if numeros % 2 == 0:
        pares += 1
    else:
        impares +=1
#Saída
for i, numeros in enumerate(lista_numeros):
    print(f"{i+1}º) número: {numeros}")

print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")

