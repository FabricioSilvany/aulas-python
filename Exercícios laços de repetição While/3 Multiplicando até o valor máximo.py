"""
Escreva um programa que multiplique um 
número inicial por um fator dado pelo 
usuário até que o produto exceda 100. 
Exiba o produto final e o número de multiplicações realizadas.
"""

import os
os.system("cls || clear")


#Declarando variáveis

contador = 0

#Solicitando dados
while True:
    numero = float(input("\nDigite um número: "))

    numero2 = float(input("Digite outro número: "))
    contador += 1

#Calculando
    multiplicacao = numero * numero2

#Exibindo dados
    if multiplicacao > 100:
        print(f"\nProduto final: {multiplicacao}")
        print(f"Quantidade de multiplicações feitas {contador}")
        break
    else:
        print("O Produto deve ser maior que 100!")


