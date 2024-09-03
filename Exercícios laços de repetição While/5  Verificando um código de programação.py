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
    promocao = input("\nDigite o código da promoção: ")
    contador += 1

    if promocao == "PROMO2024":
        print("Código aceito")
        break
    else:
        print (f"Código inválido você tentou {contador} vezes!")
    if contador == 3:
        print("\nMuitas tentativas erradas,\ntente novamente mais tarde")
        break

