"""
Escreva um algorítimo que leia três notas de um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre a média aritimética do aluno.

Após receber as notas dentro dos parâmetrps acima,
calcule a média e verifique se o aluno está aprovado,
recuperação ou reprovado considerando os seguintes critérios:

Se a média for a partir de 7, aprovado;
Se a média for emtre 5 e 6.9 o aluno está em recuperção;
Caso seja menor que 5, o aluno está reprovado.
"""

import os
os.system("cls || clear")

#Declarando variáveis

soma = 0 
QUANTIDADE_NOTAS = 3

#Solicitando dados
for i in range(QUANTIDADE_NOTAS):
    while True:
     notas = float(input(f"Digite a {i + 1}ª nota: "))

     if notas < 0 or notas > 10:
        print("\nA nota deve ser maior ou igual a 0 e menor que 10! \nDigite outra nota")
     else:
          soma += notas
          break
#Calculando

media = soma / QUANTIDADE_NOTAS

#Exibindo dados
print(f"Média {media:.1f}")

if media >= 7:
 print("Aprovado!")
elif media == 5 or media >= 6.9:
 print("Recuperação!")
else:
 print("Reprovado!")
