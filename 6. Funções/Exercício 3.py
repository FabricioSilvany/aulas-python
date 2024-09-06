"""
Crie funções que recebam 2 números e retorne
a soma, subtração, divisão e a multiplicação
destes dois números informadps.
"""
import os
os.system("cls || clear")


def calculo(subtracao, soma, divisao, multiplicacao, n1, n2):
    subtracao = print(f"\n{n1} - {n2} = {n1 - n2}")
    multiplicacao = print(f"{n1} x {n2} = {n1 * n2}")
    soma = print(f"{n1} + {n2} = {n1 + n2}")
    divisao = print(f"{n1} / {n2} = {n1 / n2}")
    
    return subtracao, multiplicacao, soma, divisao, i


for i in range(2): 
    numeros = int(input(f"Digite o {i + 1}º número: "))

resultado = calculo(subtracao=numeros, divisao=numeros, soma=numeros, multiplicacao=numeros, n1=numeros, n2=numeros)




