import os
os.system("cls || clear")

#Declarando variáveis
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

#Calculando
soma = numero1 + numero2
media = soma / 2
produto = numero1 * numero2

#Exibindo dados
print("\nExibindo Informações: ")
print(f"Media: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

if numero1 > numero2:
    print(f"Maior número: {numero1}")
else: 
    print(f"Maior número: {numero2}")

if numero1 < numero2: 
    print(f"Menor número: {numero1}")
else: 
    print(f"Menor número: {numero2}")


