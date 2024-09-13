"""
Crie um algoritimo que preencha um vetor 
com 10 números reais, calcule e mostre a
quantidade de números negativos e a soma
dos números positivos desse vetor.
"""

import os

os.system("cls || clear")

#Entrada
QUANTIDADE_NUMEROS = 4
lista_numeros = []
lista_negativos = []
lista_positivos = []

def verificar_numeros_negativos(lista_numeros):
    lista_negativos = []

    quantidade_negativos = 0

    for numero in lista_numeros:
        if numero <0:
            lista_negativos.append(numero)

    #comando len() - retorna a quantidade de elementos no vetor/lista.
    quantidade_negativos = len(lista_negativos)

    return quantidade_negativos

def verificar_numeros_positivos(lista_numeros):
    lista_positivos = []
    
    soma_positivos = 0

    for numero in lista_numeros:
        if numero > 0:
            lista_positivos.append(numero)

    #comando sum() - retorna a soma dos elementos no vetor/lista.      
    soma_positivos = sum(lista_positivos)

    return soma_positivos


for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)
    os.system("cls || clear")

#Processamento
quantidade_de_negativos = verificar_numeros_negativos(lista_numeros)
soma_de_positivos = verificar_numeros_positivos(lista_numeros)

#Saída
print(f"Quantidade de negativos: {quantidade_de_negativos}")
print(f"Soma de positivos: {soma_de_positivos}")