"""
Fazer um programa que solicita o preço de um
produto e inflaciona esse preço em 10% se ele
for menor que 100  e em 20% se ele for maior 
ou igual a 100.

Utilize uma função para obter o resultado solicitado
"""

import os
os.system("cls || clear")


#Solicitando dados
def inflacionar(preco):
    import os
    os.system("cls || clear")
    if preco < 100:
        return preco * 1.1
    else:
        return preco * 1.2
    

#Entrada
preco = float(input("Digite o preço do produto: "))

#Processamento 
preco_inflacionado = inflacionar(preco)

#Saída
print(f"Preço inflacionado: {preco_inflacionado:.2f}")