import os
os.system("cls || clear")

#Declarando variáveis

#Solicitando dados

while True:
    nota = float(input(f"Digite a nota: "))
    
    if nota < 0 or nota > 10:
        print("\nA nota deve ser maior e igual a 0 e menor que 10!")
    else:
        break #Para o laço de repetição.
    

print(f"\nNota: {nota}")
print("=====FIM=====")
