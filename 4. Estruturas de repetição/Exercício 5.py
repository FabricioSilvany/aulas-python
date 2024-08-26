import os
os.system("cls || clear")


#Declarando variáveis
media = 0

#Solicitando dados
for i in range(4):
    nota = float(input(f"Digite a {i + 1}º nota: "))

#Calculando
media = nota + media / 4

#Exibindo dados
print(f"\nMédia: {media}")

#Comandos git:  git add. / git commit -m "" / git push

