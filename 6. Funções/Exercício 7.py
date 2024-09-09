"""
Escreva um programa que permita ler  notas de um aluno e:

-Informe por meio de uma função a média;

-Informe por meio de uma função se a média for maior ou 
igual a 7, o aluno estará aprovado, caso contrário, estará
reprovado.
"""

import os
os.system("cls || clear")

def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media

def verificar_resultado(media):
    if media >= 7:
        return "Aprovado!"
    else:
        return "Reprovado!"

#Entrada
nota1 = float(input(f"Digite a 1ª nota: "))
nota2 = float(input(f"Digite a 2ª nota: "))

#Processamento
media = calcular_media(nota1, nota2)
resultado = verificar_resultado(media)

#Saida
print(f"Média: {media}")
print(f"Resultado: {resultado}")
