import os
os.system("cls || clear")

contador = 0
continua = 's'

while continua == 's':
#Comandos a serem repetidos
    print("Repetindo....")

    contador +=1
    # contador = contador + 1

    continua = input("Tecle 's' se deseja continuar: ").strip().lower()

if contador == 0:
    print(f"O bloco NÃO foi repetido")
else: 
    print(f"O bloco foi repetido {contador} vezes")

    

