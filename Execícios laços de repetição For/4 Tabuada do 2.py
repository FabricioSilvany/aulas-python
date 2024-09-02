"""
Escrevaum programa que use um laço `for`
para exibir a tabuada do 2, de 2 até 2
"""

import os
import time

os.system("cls || clear")

for i in range(0,11):
    print(f"{2} x {i} = {2 * i}")
    time.sleep(2)


