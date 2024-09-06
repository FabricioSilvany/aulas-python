"""
Crie uma função que receba um número e mostre uma mensagem 
informando se o número é par ou ímpar
"""

import os

os.system("cls || clear")

def verificador(numero):
    if numero % 2 != 0:
        print("\nO número é Ímpar")
    else:
        print("\nO número é Par")
    
    return numero

numero = int(input("\nDigite um número: "))

verificador(numero)




