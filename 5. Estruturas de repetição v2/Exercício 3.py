"""
Crie um programa que solicite ao usuário seu
login e uma senha.

O programa deve continuar pedindo o login e a senha
até que ambos estejam corretos.

O programa deve solicitar o login e senha apenas três vezes.
Caso ultrapasse o número de tentativas, o programa
deve ser finalizado.
"""

import os
os.system("cls || clear")

#Declarando variáveis

contador = 0

#Solicitando dados para cadastro
cadastro = input("Crie seu nome de usuário: ")
senha = input("Crie uma senha: ")

#Verificando se o login corresponde aos dados

while True:
  login_usuario = input("\nDigite o seu nome de usuário: ")
  login_senha = (input("Digite sua senha: "))
  contador += 1

  if login_usuario == cadastro and login_senha == senha:
    print("\nBem vindo!")
    break
  else:
    print("\nLogin ou senha incorretos!")
    print(f"Tentativa: {contador} \n")
    if contador == 3:
      print("Muitas tentativas. Tente novamente mais tarde!")
      break
   