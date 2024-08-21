import os
os.system("cls || clear")

#Declarando variáveis e solicitando dados

idade = int(input("Digite sua idade: "))

#Verificando e exibindo dados

if idade < 18 or idade >= 65:
    print("Não precisa votar!")
else:
    print("É necessário votar!")