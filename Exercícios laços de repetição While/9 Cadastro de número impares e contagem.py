"""
Crie um programa que peça ao usuário para
inserir números inteiros até que a soma
dos números ímpares inseridos seja maior que 200.
O programa deve exibir o total de números
ímpares inseridos e a soma desses números. 
"""

import os
os.system("cls || clear")

#Declarando variáveis
contador = 0
soma = 0
impares = 0
pares = 0

#Solicitando dados
print("Insira números até que a soma dos impares seja maior ou igual a 200!")

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 !=0:
        impares += numero
        contador += 1
    else:
        pares += 1

    soma += impares

    if soma >= 200:
        print(f"\nQuantidade de números ímpares {contador}")
        print(f"Quantidade de números pares {pares}")
        print(f"Soma dos números {soma}")
        break


