"""
Crie um algotítimo que leia 5 números
inteiros e, em seguida, mostre na tela:

1. A quantidade de números pares e ímpares;
2. A quantidade de números positivos e negativos;
3. A quantidade de números inseridos.
"""

import os

os.system("cls || clear")

#Entrada
numeros_gerais = []
numeros_pares = []
numeros_impares = []
numeros_positivos = []
numeros_negativos = []

def verificador_pares(lista_numeros):
    if numeros % 2 == 0:
        numeros_pares.append(numeros)

    return numeros_pares

def verificador_impares(lista_numeros):
    if numeros % 2 == 1:
        numeros_impares.append(numeros)
    
    return numeros_impares

def verificador_positivos(lista_numeros):
    if numeros > 0:
        numeros_positivos.append(numeros)

    return numeros_positivos

def verificador_negativos(lista_numeros):
    if numeros < 0:
        numeros_negativos.append(numeros)

    return numeros_negativos

for i in range(5):
    numeros = int(input(f"Digite o {i+1}º número: "))
    numeros_gerais.append(numeros)
    os.system("cls || clear")

#Pocessamento

quantidade_pares = verificador_pares(numeros_gerais)
quantidade_positivos = verificador_positivos(numeros_gerais)
quantidade_negativos = verificador_negativos(numeros_gerais)
quantidade_impares = verificador_impares(numeros_gerais)
#Saída
print("...Exibindo dados...")

print(f"""
Quantidade de números gerais: {len(numeros_gerais)}
Quantidade de números pares: {len(quantidade_pares)}
Quantidade de números impares: {len(quantidade_impares)}
Quantidade de números positivos: {len(quantidade_positivos)}
Quantidade de números negativos: {len(quantidade_negativos)}
""")