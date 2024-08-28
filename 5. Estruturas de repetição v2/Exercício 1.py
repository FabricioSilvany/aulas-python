"""
Escreva um algorítimo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre a média aritimética do aluno.
"""

import os
os.system("cls || clear")

#Solicitando dados
while True:

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    if nota1 and nota2 < 0 or nota1 and nota2 > 10:
            print("A nota não pode ser menor que 0 e não pode ser maior que 10!")
    else:
        break

media = (nota1 + nota2) / 2
print(f"\nMedia: {media}")

    






