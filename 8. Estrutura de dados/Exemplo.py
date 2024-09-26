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