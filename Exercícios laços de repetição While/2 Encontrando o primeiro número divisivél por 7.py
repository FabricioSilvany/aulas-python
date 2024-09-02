"""
Escreva um programa que use um laço while
para encontrar o primeiro número maior
que 50 que seja divisível por 7.
Exiba esse número.
"""

import os
os.system("cls || clear")

#Solicitando dados
while True:
    numero = float(input("Digite um número: "))

    if numero > 50 and numero / 7:
        print(f"Número {numero}")
        print(f"Divisão: {numero / 7}")
        break
