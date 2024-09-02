"""
Desenvolva um programa que solicite ao usuário inserir
um código de promoção para obter um desconto.
O código correto é "PROMO2024".
O usuário tem 3 tentativas para acertar o código.
Se o código estiver correto,
exiba uma mensagem de "Código aceito" e o desconto.
Se o usuário errar o código nas 3 tentativas,
exiba uma mensagem de "Código inválido".
"""

import os
os.system("cls || clear")

#Declarando variáveis

contador = 0

#Solicitando dados
while True:
    promocao = input("Digite o código da promoção: ")
    contador += 1

    if promocao == "PROMO2024":
        print("Código aceito")
        break
    else:
        print ("\nCódigo inválido você ainda tem 3 tentativas!")
    if contador == 0:
        print("Muitas tentativas erradas,\ntente novamente mais tarde")

