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

for i in range(2):
    while True:
        print("Digite um número inteiro, positivo e par")
        numeros = int(input(f"Digite o {i+1}º número: "))
        os.system("cls || clear")

        if numeros < 0 and numeros % 2 == 0:
            lista_numeros_positivos_pares.append(numeros)
        
#Processamento
        break

#Saída
print("----Exibindo dados----")
for numero in reversed(lista_numeros):
    print(f"Número inserido: {numero}")