from aulaclasse import *
from views import *

lista_humano = []
lista_cachorro = []


def criar_pessoa():
    nome = input("Nome da pessoa: ")
    nacionalidade = input("Nacionalidade: ")
    cpf = input("CPF: ")
    tamanho = input("Tamanho em M: ")
    pessoa = Humano(nome, nacionalidade, cpf, tamanho)
    lista_humano.append(pessoa)

def criar_cao():
    nome = input("Nome do cão: ")
    tamanho = input("Tamanho em CM: ")
    raca = input("Raça: ")
    cor = input("Cor: ")
    peso = input("Peso: ")
    cao = Cachorro(nome, tamanho, raca, cor, peso)
    lista_cachorro.append(cao)

def listar(lista):
    for objeto in lista:
        print(objeto.info())


while True:
    menu_principal()
    op = int(input("Escolha uma opção: "))
    if 1 == op:
        criar_pessoa()
    elif 2 == op:
        criar_cao()
    elif 3 == op:
        listar(lista_humano)
    elif 3 == op:
        listar(lista_cachorro)    