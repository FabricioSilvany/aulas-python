"""
Escreva um algorítimo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre a média aritimética do aluno.
"""

import os
os.system("cls || clear")

#Declarando variáveis
QUANTIDADE_NOTAS = 2
soma = 0

#Solicitando dados
for i in range(QUANTIDADE_NOTAS):
   while True:
        nota = float(input(f"Digite a {i + 1}ª nota: "))  

        if nota >=0  and nota <= 10:
          break
   soma += nota

media = soma / QUANTIDADE_NOTAS

print(f"\nMedia: {media}")

    






