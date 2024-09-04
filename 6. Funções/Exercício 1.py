import os
os.system("cls || clear")

#Declarando funções

def medir(n1, n2):
    os.system("cls || clear")
    media = (n1 + n2) / 2
    return media

#Solicitando dados

nota_1 = float(input(f"Digite a primeira nota: "))
nota_2 = float(input(f"Digite a segunda nota: "))


media = medir(nota_1 , nota_2)

print(f"Primeira nota: {nota_1}")
print(f"Segunda nota: {nota_2}")
print(f"Média: {media}")

