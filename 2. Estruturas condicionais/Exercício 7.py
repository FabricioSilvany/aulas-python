import os
os.system("cls || clear")

#Solicitando dados
print("""
Dias da semana:

1 - Domingo
2 - Segunda-Feira
3 - Terça-Feira
4 - Quarta-Feira
5 - Quinta-Feira
6 - Sexta-Feira
7 - Sábado                                      
      """)

dia = int(input("Digite o dia da semana: "))

#Verificando

match(dia):
    case 1:
        print("Final de semana")
    case 2: 
         print("Dia útil")
    case 3:
         print("Dia útil")
    case 4:
         print("Dia útil")
    case 5: 
         print("Dia útil")
    case 6:
         print("Dia útil")
    case 7:
         print("Final de semana")
    case _:
        print("Opção inválida")

#Exibindo dados
