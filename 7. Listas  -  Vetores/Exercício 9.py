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

while True:
    print("Para encerrar digite 0")
    numeros = int(input(f"Digite um número: "))
    numeros_gerais.append(numeros)
    os.system("cls || clear")

#Pocessamento
    if numeros > 0:
        numeros_positivos.append(numeros)

    elif numeros < 0:
        numeros_negativos.append(numeros)

    if numeros % 2 == 0:
        numeros_pares.append(numeros)
    
    elif numeros % 2 ==1:
        numeros_impares.append(numeros)
    
    if numeros == 0:
        break

#Saída
print("...Exibindo dados...")

print(f"""
Quantidade de números gerais: {len(numeros_gerais)}
Quantidade de números pares: {len(numeros_pares)}
Quantidade de números impares: {len(numeros_impares)}
Quantidade de números positivos: {len(numeros_positivos)}
Quantidade de números negativos: {len(numeros_negativos)}
""")