import os
os.system("cls || clear")

#Declarando variáveis
soma = 0
contador = 0

#Solicitando informações
while True:
    for i in range(2):
        notas = float(input(f"\nDigite a {i+1}ª nota: "))
        soma += notas
        contador += 1

    print("""\nDeseja adicionar outra nota?
S = Sim
N = Não""")
    
    opcao = input("\nDigite uma opção: ").upper()

    if opcao == "N":
        break

media = soma / contador
print(f"Média {media}")







     
       




