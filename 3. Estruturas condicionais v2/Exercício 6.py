import os
os.system("cls || clear")

#Declarado variáveis
peso_ideal = 0
#Solicitando dados

print("""
Escolha uma opção: 

F = Feminino
M = Masculino   
      """)

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (M ou F): ")

match sexo:
    case "F" | "f":
        peso_ideal = (62.1 * altura) - 44.7
    case "M" | "m":
        peso_ideal = (72.7 * altura) - 58
    case _:
        print("Opção inválida.")

print(f"Peso ideal: {peso_ideal:.2f}") 
  