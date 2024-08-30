"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota.
Mostre um menu conforme o descrito abaixo:

S – Inserir mais uma nota;
P – Ver quantas notas foram inseridas;
N – Calcular a média aritmética das notas informadas.
"""
import os
import time
os.system("cls || clear")

#Declarando variáveis
soma = 0
contador = 0
#Solicitando informações
while True:
    for i in range(2):
        notas = float(input(f"Digite a {i+1}ª nota: "))
        soma += notas
        contador += 1
        media = soma / contador

    print("""\nDeseja adicionar mais uma nota?
S = Sim
P = Ver quantas notas foram inseridas
N = Não, apenas calcule a média""")
    
    opcao = input("\nDigite uma opção: ").upper()

    match(opcao):
        
        case "S":
         notas = float(input("\nDigite mais uma nota: "))
         print(f"Média {media:.1f}")
         break
       
        case "N":
         print(f"Média {media:.1f}")
         break
   
        case "P":
          print(f"\nNotas inseridas: {contador}")
          time.sleep(2)
       
        case _:
          print("Opção inválida")
          time.sleep(2)