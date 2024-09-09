"""
Crie um programa que
leia 6 números por meio de uma
função:
- Quantos números são pares
- Quantos números são impares
"""

import os

os.system("cls || clear")


def verificador():

    impares = 0
    pares = 0

    for i in range(6):
        numero = int(input(f"Digite o {i + 1}º número: "))
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Quantidade de números ímpares: {impares} ")
    print(f"Quantidade de números pares: {pares}")


verificador()





