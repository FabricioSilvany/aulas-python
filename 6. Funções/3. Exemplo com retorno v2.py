import os
os.system("cls || clear")

#Função com retorno - return
def descontos_salario(salario_bruto):
    os.system("cls || clear")
    vale_transporte = 200
    vale_refeição = 100
    plano_de_saude = 300

    resultado = salario_bruto - (vale_transporte + vale_refeição + plano_de_saude)

    return resultado

salario_bruto = float(input("Digite o valor de seu salário bruto: "))

salario_liquido = descontos_salario(salario_bruto)

print(f"Salário líquido {salario_liquido}")