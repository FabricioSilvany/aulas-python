"""
Crie um programa que solicite ao usuário
criar uma senha. O programa deve então
pedir para confirmar a senha e
garantir que ambas as senhas coincidam.
Se as senhas não coincidirem, o programa 
deve continuar pedindo para o usuário inserir
e confirmar a  tenha até que ambas sejam iguais
"""

import os
os.system("cls || clear")

#Solicitando criação de dados
usuario = input("\nCrie seu nome de usuário: ")
senha = input("Crie uma senha: ")

#Confirmando dados
while True:
    usuario_salvo = input("\nDigite seu nome de usuário: ")
    senha_salva = input("Digite sua senha: ")

    if senha_salva == senha and usuario_salvo == usuario:
        print("\nBem Vindo!")
        break
    else:
        print("\nNome de usuário ou senha inválidos!")
