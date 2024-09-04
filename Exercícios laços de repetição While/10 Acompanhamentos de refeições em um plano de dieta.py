"""
Crie um programa que permita ao usuário registrar
o número de calorias consumidas em cada refeição.
O programa deve continuar registrando as calorias
até que o total de calorias consumidas
ultrapasse 2000 calorias. Após exceder
2000 calorias, exiba o total de calorias
consumidas e o excesso.
"""

import os
os.system("cls || clear")

#Declarando variáveis

calorias = 0

#Solicitando dados
print("Registre o número de calorias consumidas até que seja igual ou maior a 2000")


while True:
    calorias += float(input("Digite o total de calorias consumidas hoje: "))
    excesso = calorias - 2000

    if calorias >= 2000:
        print(f"\nCalorias consumidas {calorias}")
        print(f"Excesso {excesso}")
        break
