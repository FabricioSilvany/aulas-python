"""
Escreva um programa que utilize um laço for
para multiplicar cada número
de 1 a 6 por 3 e exibir o resultado.
"""

import os 
import time

os.system("cls || clear")

for i in range(1,7):
    print(f"{3} x {i} = {3 * i}")
    time.sleep(2)