"""
Crie funções que recebam 2 números e retorne
a soma, subtração, divisão e a multiplicação
destes dois números informadps.
"""
import os
os.system("cls || clear")


def calculo(subtracao, soma, divisao, multiplicacao, n1, n2):
    opcao = input("""
Escolha uma opção:

Soma = (+)
Subtração = (-) 
Divisão = (/)
Multiplicação = (*)     

""")
    match(opcao):
        case "-":
            subtracao = print(f"\n{n1} - {n2} = {n1 - n2}")
        case "*":
            multiplicacao = print(f"\n{n1} x {n2} = {n1 * n2}")
        case "+":
            soma = print(f"\n{n1} + {n2} = {n1 + n2}")
        case "/":
            divisao = print(f"\n{n1} / {n2} = {n1 / n2}")
        case _:
            print("Opção inválida")
    
    return subtracao, multiplicacao, soma, divisao, i, opcao


for i in range(2):
    os.system("cls || clear")
    numeros = int(input(f"Digite o {i + 1}º número: "))


calculo(multiplicacao=numeros, soma=numeros, divisao=numeros, subtracao=numeros, n1=numeros, n2=numeros)


