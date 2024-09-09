"""
Escreva um programa que solicite ao usuário
o ano de nascimento, e utilizando uma função
retorne com a idade do usuário
"""

import os
os.system("cls || clear")

ano_atual = 2024

def calcular_idade(idade):
    idade = ano_atual - ano_de_nascimento
    return idade

#Entrada
ano_de_nascimento = int(input("Digite seu ano de nascimento: "))

#Processamento 
idade = calcular_idade(ano_de_nascimento)

#Saida
print(f"Idade {idade}")
