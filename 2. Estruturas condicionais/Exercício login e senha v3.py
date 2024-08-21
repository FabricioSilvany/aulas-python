import os
os.system("cls || clear")

#Solicitando dados
login = input("Escreva seu login: ")
senha = input("Escreva sua senha: ")

#Verificando e exibindo dados
login_correto = login == "marta" #true
senha_correta = senha == "123" #false

if login_correto and senha_correta:
    print("Bem vindo!")
else:
    print("Login ou senha inválidos")
