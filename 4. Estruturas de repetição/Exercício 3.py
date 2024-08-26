import os
os.system("cls || clear")

#Declarando variáveis
soma = 0

#Solicitando dados
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número "))
    soma = soma + numero

print(f"Soma dos números: {soma}")
