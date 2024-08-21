import os
os.system("cls || clear")

#Soliciatando dados.

print("""
Cardápio:
      
1 - Picanha
2 - Lasanha
3 - Strogonoff
4 - Bife acebolado
5 - Pão com ovo  
      """)

prato = int(input("Digite o número do prato desejado: "))

#Exibindo dados

match(prato):
    case 1:
        print("Picanha: R$25.00")
    case 2:
        print("Lasanha: R$20.00")
    case 3:
        print("Strogooff: R$18.00")
    case 4:
        print("Bife acebolado: R$15.00")
    case 5: 
        print("Pão com ovo: R$5,00")
    case _:
        print("Opção inválida!")
