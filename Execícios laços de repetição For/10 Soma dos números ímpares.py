"""
Escreva um programa que calcule a soma
dos números ímpares de 1 a 9
utilizando um laço `for`.
"""

import os
import time

os.system("cls || clear")

soma = 0
for i in range(1,10,2):
    soma += i
    print(f"{soma}")


