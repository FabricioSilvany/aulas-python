"""
Crie um programa que use um laço `for`
para gerar e exibir os quadrados dos
números de 1 a 5 (ou seja, 1², 2², 3², etc.).
"""

import os
import time

os.system("cls || clear")

for i in range(1,6):
    print(f"{i} x {i} = {i * i}")
    time.sleep(2)