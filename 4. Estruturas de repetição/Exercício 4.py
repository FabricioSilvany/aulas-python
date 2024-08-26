import os
os.system("cls || clear")


#Declarando variáveis

pares = 0
impares = 0

#Solicitando dados

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

#Exibindo dados
print(f"\nQuantidade de pares: {pares}")
print(f"\nQuantidade de ímpares: {impares}")