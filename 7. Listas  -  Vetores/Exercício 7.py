"""
Crie um algoritimo que receba do usuário
valores e armazene em um vetor 5 números
caseo seja informado um valor um valor negativo
atribua o valor .

-Liste os valores de vetor.
"""

import os

os.system("cls || clear")

#Entrada
lista_numeros = []

def atribuindo_zero(lista_numeros):
    lista_atualizada = []

    #Verificando se o número é negtivo

    for numero in lista_numeros:

        #Caso o número seja negativo ele vai ser substituido por zero
        if numero < 0:
            numero = 0

        #Inserindo número no vetor
        lista_atualizada.append(numero)

    return lista_atualizada

for i in range(5):
    print("--Solicitando dados--")
    numeros = int(input(f"Digite o {i+1}º número: "))
    os.system("cls || clear")
    
    lista_numeros.append(numeros)

#Processamento 
lista_numeros = atribuindo_zero(lista_numeros)

#Saída
print("---Exibindo dados---")

for i, numero in enumerate(lista_numeros):
    print(f"{i+1}º número digitado: {numero}")