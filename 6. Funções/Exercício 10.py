"""
Escreva um programa que solicite ao
utilizador o fornecimento do seu peso
em kg e de sua altura em m e a partir 
deles calcule o índice de massa corpórea
do utilizador.
"""

import os
os.system("cls || clear")

#Declarando funções
def calcular_massa(peso, altura):
    return peso / (altura **2)

#Entrada
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

#Processamento
imc = calcular_massa(peso, altura)

#Saida
print(f"Seu índice de massa corporal é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso \nConsulte um nutricionista para orientação")
elif imc >= 18.5 and imc < 24.9:
    print("Peso normal \nMantenha hábitos saudáveis!")
elif imc >= 25 and imc < 29.9:
    print("Sobrepeso \nConsidere uma dieta balanceada e atividade física")
elif imc >= 30 and imc < 34.9:
    print("Obesidade grau 1 \nProcure orientação de um profissional de saúde")
elif imc >= 35 and imc < 39.9:
    print("Obesidade grau 2 \nConsulte um médico para avaliação e orientação")
elif imc >= 40:
    print("Obesidade grau 3 \nBusque assistência médica imediatamente")


