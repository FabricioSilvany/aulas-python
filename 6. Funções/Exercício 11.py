"""
Faça uma função que receba a idade de uma pessoa
em anos, meses e dias e retorna essa idade expressa em
dias.
"""

import os

os.system("cls || clear")

#Funções
def calcular_idade(meses,dias,anos):
    resultado = (anos * 365) + (meses * 30.437) + dias
    return resultado

#Entrada
anos = int(input("Digite quantos anos você tem: "))
mes_de_nascimento = float(input("Digite seus meses de vida: "))
dia_de_nascimento = int(input("Digite seus dias de vida: "))

#Processamento 
idade = calcular_idade(mes_de_nascimento, dia_de_nascimento, anos)

#Saida
print(f"Idade em dias: {idade:.2f}")
