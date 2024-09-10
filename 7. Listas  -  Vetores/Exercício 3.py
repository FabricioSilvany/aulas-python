"""
Crie um programa que leia 4 notas,
armazenando em um vetor e calcule a
média aritimética.

Verifique a situação do aluno considerando:
-Média maior ou igua a 7: Aprovado
-Média maior ou igual a 5: Recuperação
-Média menor que 5: Reprovado

Mostre as 4 notas informadas pelo usuário e informa a média.
"""

import os

os.system("cls || clear")

#Variáveis e constantes
soma = 0
QUANTIDADE_NOTAS = 4

#Funções
def situacao_do_aluno():
    if media >= 7:
        return "Aprovado!"
    elif media >= 5:
        return "Recuperação!"
    else:
        return "Reprovado!"

#Entrada
lista_notas = []

for i in range(4):
    notas = float(input(f"Digite a {i + 1}ª nota: "))
    lista_notas.append(notas)
    os.system("cls || clear")

#Processamento
soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

verificando = situacao_do_aluno()

for i, nota in enumerate(lista_notas):
    print(f"{i + 1}ª nota: {notas}")

print(f"\nMédia {media}")
print(f"Situação do aluno: {verificando}")

