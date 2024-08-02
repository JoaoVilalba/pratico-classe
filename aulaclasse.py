class Animal:
    nome: str
    instinto: bool
    coracao: bool
    racional: bool

    def __init__(self, nome, coracao):
        self.nome = nome
        self.coracao = coracao

class Humano(Animal):
    nacionalidade: str
    cpf: str
    tamanho: float

    def __init__(self, nome, nacionalidade, cpf, tamanho):
        super().__init__(nome, True, True)
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.cpf = cpf
        self.tamanho = tamanho
        self.instinto = True
        self.coracao = True
        self.racional = True

class Cachorro(Animal):
    tamanho: float
    raca: str
    cor: str
    peso: float

    def __init__(self, nome, tamanho, raca, cor, peso):
        super().__init__(nome, True, False)
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.instinto = True
        self.coracao = True
        self.racional = False

    def latir(self):
        print('au-au-au')

# cao = Cachorro('Thanos', 0.75, 'pitbull', 'preto', 51)

# pessoa = Humano('joao', 'espanhol', '111.222.333.00', 1.92)

# print(f"\nCachorro:\nNome: {cao.nome}\nTamanho: {cao.tamanho}\nRaça: {cao.raca}\nCor: {cao.cor}\nPeso: {cao.peso}")
# (cao.latir())
# print(f"\n\nPessoa:\nNome: {pessoa.nome}\nNacionalidade: {pessoa.nacionalidade}\nCpf: {pessoa.cpf}\nTamanho: {pessoa.tamanho}")
