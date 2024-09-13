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
lista_positivos = []
lista_negativos = []

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)
    os.system("cls || clear")

#Processamento
    if numero <0:
        lista_negativos.append(numero)
    else:
        lista_positivos.append(numero)

#comando len() - retorna a quantidade de elementos no vetor/lista.
quantidade_negativos = len(lista_negativos)

#comando sum() - retorna a soma dos elementos no vetor/lista.
soma_positivos = sum(lista_positivos)

#Saída
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Soma de positivos: {soma_positivos}")