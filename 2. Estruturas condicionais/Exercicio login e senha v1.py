import os
os.system("cls || clear")

#Declarando variáveis e solicitando dados

login = input("Escreva seu login: ")
senha = input("Escreva sua senha: ")

#Verificando e exibindo dados

if login == "Usuário" and senha == "123456":
    print("Bem vindo!")
else:
    print("Login ou senha inválidos")
