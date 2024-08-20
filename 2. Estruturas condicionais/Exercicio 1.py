import os 
os.system("cls || clear")

#Solicitando dados.
nome  = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

#Verificando.
media = (nota + nota2 + nota3) / 3

#Exibindo dados.
print("\nExibindo Resultados: ")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {nota}")
print(f"Segunda Nota: {nota2}")
print(f"Terceira Nota: {nota3}")
print(f"Media: {media}")

if media >= 7:
    print("Aprovado!")

else:
    print("Reprovado!")
    







