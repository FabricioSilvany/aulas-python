import os
os.system("cls || clear")

#Declarando variáveis
soma = 0

#Solicitando dados
for i in range(5):
    numero = int(input("Digite um número: "))
    soma = soma + numero

#Calculando
print(f"Soma dos números: {soma}")
