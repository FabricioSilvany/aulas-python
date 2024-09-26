import os
from dataclasses import dataclass

os.system("cls || clear")

#Estrutura de dados.
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_CLIENTES = 4

lista_de_clientes = []

#Salvar em um arquivo chamado:carteira_de_clientes.txt

#Fazer leitura de dados do arquivo carteira_de_clientes.txt mostrando no terminal.

print("=== Solicitando dados dos clientes ===")

for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome = input("Insira seu nome: "),
        sobrenome = input("Insira seu sobrenome"),
        idade = int(input("Insira sua idade: ")),
        peso = float(input("Insira seu peso: ")),
        altura = float(input("Insira sua altura: "))
    )
    os.system("cls || clear")
    lista_de_clientes.append(cliente)


nome_do_arquivo = "Carteira_de_clientes.txt"

with open(nome_do_arquivo, "a") as arquivo_clientes:
    for cliente in lista_de_clientes:
        arquivo_clientes.write(f"{cliente.nome},{cliente.sobrenome} {cliente.idade}, {cliente.peso}, {cliente. altura}\n")

#Lendo dados do arquivo
with open(nome_do_arquivo, "r") as lendo_arquivos:
    for linha in lendo_arquivos:
        nome, sobrenome,  idade, peso, altura = linha.strip().split(",")
        lista_de_clientes.append(Cliente(nome = nome, sobrenome = sobrenome, idade = int(idade), altura = float(altura), peso = float(peso)))

#Limpando listas de clientes
lista_de_clientes = []

#Fechando conexão com a lista de clientes
arquivo_clientes.close()

#Exibindo dados dos clientes
print("==== Exibindo dados ====")
for clientes in lista_de_clientes:
    print(f"""
Nome: {cliente.nome}
Sobrenome: {cliente.sobrenome}
Idade: {cliente.idade}
Peso: {cliente.peso}
Altura: {cliente.altura}
""")