"""
Crie um programa que
leia 6 números por meio de uma
função:
- Quantos números são pares
- Quantos números são impares
"""

import os

os.system("cls || clear")


contador = 0

def verificador(numero):
    impares = 0
    pares = 0

    if numero % 2 !=0:
        impares += 1
    else:
        pares += 1
    
    print(f"Quantidade de números: {contador}")
    print(f"Quantidade de números ímpares: {impares} ")
    print(f"Quantidade de números pares: {pares}")

    return numero, contador, pares, impares

for i in range(6):
    numero = int(input(f"Digite o {i + 1}º número: "))
    contador += 1

verificador(numero)





