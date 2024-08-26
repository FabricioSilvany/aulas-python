import os
os.system("cls || clear")

#Declarando variáveis

soma = 0

#Constante

QUANTIDADE_NOTAS = 3

#Solicitando dados

for i in range(QUANTIDADE_NOTAS):
    notas = float(input(f"Digite a {i + 1}º nota: "))
    soma = notas + soma

#Calculando

media = soma / QUANTIDADE_NOTAS

#Exibindo dados

if media >= 7:
    print("Aprovado!")
elif media >= 4: 
    print("Recuperação")
else:
    print("Reprovado!")
    
print(f"\nMédia {media}")


