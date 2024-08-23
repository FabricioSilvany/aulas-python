import os
os.system("cls || clear")

#Mostrando opções para o usuário
print("""
Opções:
            
* = Multiplicação 
- = Subtração
+ = Soma
/ = Divisão
      """)

#Declarando variáveis e solicitando dados
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

opcao = input("Digite uma opção: ")

#Calculando e exibindo dados
match(opcao):
    case "*":
        print(f"Resultado: {numero1 * numero2}")
    case "-":
        print(f"Resultado: {numero1 - numero2} ")
    case "+":
        print(f"Resultado: {numero1 + numero2} ")
    case "/":
        print(f"Resultado: {numero1 / numero2}")
    case _:
        print("Opção inválida.")
    
        print("====FIM=====")
        