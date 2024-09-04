"""
Crie um programa para ajudar o usuário
a acompanhar suas metas de estudo.
O usuário define uma meta de horas de
estudo e o programa deve permitir que o usuário insira
o número de horas estudadas até que o total atinja
ou exceda a meta. O programa deve  exibir o total
de horas estudadas e o valor excedente.
"""

import os
os.system("cls || clear")

#Declarando variáveis

horas = 0

#Solicitando dados

meta = float(input("\nDigite uma meta de horas: "))

while True:
    horas += float(input("\nInsira as horas estudadas hoje: "))

    tempo_restante = meta - horas

    if horas >= meta:
        print("Meta atingida!")
        print(f"Horas estudadas: {meta + horas}")
        break
    else:
        print(f"\nAinda restam: {tempo_restante}")
