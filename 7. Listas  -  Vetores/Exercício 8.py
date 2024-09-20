"""
Crue um algoritimo que aceite apenas 
6 valores inteiros, positivos e pares
em seguida, mostre na tela os valores 
lidos na ordem iversa.

Caso seja informado um número diferente
dos critérios apresentados acima, repita 
a pergunta para o usuário.
"""

import os

os.system("cls || clear")

#Entrada
lista_numeros_positivos_pares = []

for i in range(6):
    while True:
        print("\nDigite um número inteiro, positivo e par")
        numeros = int(input(f"Digite o {i+1}º número: "))
        os.system("cls || clear")

        if numeros > 0 and numeros % 2 == 0:
            lista_numeros_positivos_pares.append(numeros)
            break
        else:
            print("Número inserido inválido!")
        

#Saída
print("----Exibindo dados----")
for i, numero in enumerate(reversed(lista_numeros_positivos_pares)):
    print(f"{len(lista_numeros_positivos_pares) - i}º número: {numero}")