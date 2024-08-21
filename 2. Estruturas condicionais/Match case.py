import os
os.system("cls || clear")

print("""
1 - Cadastrar usuário
2 - Excluir usuário
3 - Sair do sistema    
      """)

opcao = int(input("Digite uma opção: "))

match(opcao):
    case 1:
        print("Opção de cadastrar usuário.")
    case 2:
        print("Opção de excluir usuário.")
    case 3:
        print("Opção de sair do sistema.")
    case _:
        print("Opção inválida.")

        print("====FIM====")

