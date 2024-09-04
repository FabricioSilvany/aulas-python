import os

os.system("cls || clear")

#Função com retorno

def somar(n1, n2):
    soma = n1 + n2
    return soma


numero_1 = int(input("Digire um número:"))
numero_2 = int(input("Digire um número:"))

soma = somar(numero_1 + numero_2)

print(f"Soma {soma}")

