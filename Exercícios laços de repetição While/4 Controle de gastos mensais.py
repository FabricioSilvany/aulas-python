"""
Crie um programa que ajude um usuário
a controlar seus gastos mensais.
O programa deve permitir que o usuário insira gastos
diários até que o total gasto no mês exceda
um orçamento inicial fornecido.
O programa deve exibir o total gasto e o valor  excedente.
"""

import os
os.system("cls || clear")

gastos = 0

#Solicitando dados
limite = float(input("Digite qual o limite que você quer gastar: "))

while True:

    gastos += float(input("\nDigite seus gastos diários: "))
    restante = limite - gastos

#Calculando gastos
    if gastos > limite:
        print("\nLimite de gastos excedido!")
        break

    else:
        print(f"Ainda restam: {restante}") 