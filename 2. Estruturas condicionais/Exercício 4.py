import os
os.system("cls || clear")

#Declarando variáveis e solicitando dados
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

#Calculando e exibindo dados
print("\nExibindo dados:")
print(f"\nPrimeiro número: {numero1}")
print(f"Segundo número: {numero2}")

if numero1 > numero2: 
    print(f"Maior número: {numero1}")
    print(f"Menor número: {numero2}")
else:
    print(f"Maior número: {numero2}")
    print(f"Menor número: {numero1}")
