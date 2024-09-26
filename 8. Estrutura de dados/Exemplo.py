import os
from dataclasses import dataclass

os.system("cls || clear")

#Estrutura de dados
@dataclass
class Aluno:
    nome: str
    idade: int


QUANTIDADE_ALUNOS = 2

lista_de_alunos = []

print("\n=== Solicitando dados dos alunos ===")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Insira seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    lista_de_alunos.append(aluno)

print("\n=== Exibindo dados dos alunos ===")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")



#Definido arquivo para salvar os dados
nome_do_arquivo = "Lista_de_alunos_SENAI.txt"

#Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "w") as arquivo_alunos:
#Percorredo vetor/lista.    
    for aluno in lista_de_alunos:
#Escrevendi no arquivo uma linha de cada vez.        
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")

print("\n=== Dados dos alunos salvo com sucesso! ===")

#CRUD

#[X]CREATE
#READ
#UPDATE
#DELETE