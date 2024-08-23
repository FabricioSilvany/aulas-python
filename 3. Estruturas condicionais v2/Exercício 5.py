import os
os.system("cls || clear")

#Solicitando dados
print("""
Escolha uma opção:

1 - Á Vista.
2 - Pagamento á prazo.
      """)

#Verificando e exibindo dados
pagamento = int(input("Digite um número para a opção: "))

match pagamento:
    case 1:
        print("Desconto de 10%!")
        print("""\nValor do produto: R$100.00
Forma de pagamento: Á vista
Valor do desconto: R$10.00
Total a pagar: R$90.00""")
    case 2:
        parcelas = int(input("Quantas parcelas deseja pagar (Limite até 6!): "))
        if parcelas > 6:
            print("Valor inválido!")
        else:
            print(f"""\nValor do produto: R$100.00
Forma de pagamento: Á prazo
Quantidade de parcelas: {parcelas}
Valor da parcela: R$:16.66
Total á prazo: R$100.00""")
    case _:
        print("Opção inválida!")