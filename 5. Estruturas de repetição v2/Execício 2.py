"""
Crie um programa que solicite ao usuário seu
login e uma senha.

O programa deve continuar pedindo o login e a senha
até que ambos estejam corretos.
"""

import os
os.system("cls || clear")

#Solicitando dados para cadastro
cadastro = input("Crie seu nome de usuário: ")
senha = input("Crie uma senha: ")

#Verificando se o login corresponde aos dados
while True:
      
    login_usuario = input("\nDigite o seu nome de usuário: ")
    login_senha = (input("Digite sua senha: "))

   
    if login_usuario == cadastro and login_senha == senha:
        print("\nBem vindo!")
        break
    else: 
        print("\nLogin ou senha incorretos!")
