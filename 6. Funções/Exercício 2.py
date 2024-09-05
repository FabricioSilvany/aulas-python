"""
Faça um programa que imprima a tabuada
de um número informado pelo usuário de 1 a 10 
utilizando uma função para exibir o resultado
"""

import os
import time

os.system("cls || clear")

#Função def
def tabuada(n1,n2):
    calculo = n1 * n2
    montante = print(f"{n1} x {n2} = {n1 * n2}")
    return calculo, montante



#Solicitando dados
numero = int(input("Digite um número: "))

for i in range(1,11):
    montante = tabuada(numero, i)
    time.sleep(2)

