class Carro:
    carros =[]
    def __init__(self, modelo, cor, ano) -> None:
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo} || {carro.cor} || {carro.ano}')
            
carro1 = Carro('HB20', 'preto', 2020)

Carro.listar_carros()

class Restaurante:
    def __init__(self, nome, categoria, rodizio, aceita_vr) -> None:
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.rodizio = rodizio
        self.aceita_vr = aceita_vr
    def __str__(self) -> str:
        return f'{self.nome} | {self.categoria}'
        
restaurante_minek = ('Minek', 'Japonês', 'Sim', 'Sim')


class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

minek = Cliente('Minek', 27)
seijao = Cliente('Seijao', 27)
pablera = Cliente('Pablera', 26)


class Pessoa:
    pessoas = []
    def __init__(self, nome='', idade=0, profissao='') -> None:
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)
    
    def __str__(self) -> str:
        return f'Nome: {self.nome}\nIdade: {self.idade}\nProfissão: {self.profissao}'
    
    def aniversario(self):
        self.idade +=1
        
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá {self.nome}! Meu nobre {self.profissao}'
        else:
            return f'Olá {self.nome}!'

    @classmethod
    def listar_pessoas(cls):
        for pessoa in Pessoa.pessoas:
            print(f'Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nProfissão: {pessoa.profissao}\n\n')


saes = Pessoa('Saes', 28, 'Programador')
pablera = Pessoa('Pablo', 27, 'UX/UI Designer')
salem = Pessoa('Salem o gato', 8)

print(saes)
print(pablera)
print(salem)

print(saes.saudacao)
print(pablera.saudacao)
print(salem.saudacao)

saes.aniversario()
pablera.aniversario()
salem.aniversario()

Pessoa.listar_pessoas()