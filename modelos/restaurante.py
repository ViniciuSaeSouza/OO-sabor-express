from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self) -> str:
        return f'{self._nome} || {self._categoria} || {self._ativo}'
    
    @property
    def ativo(self):
        return 'Ativo✅' if self._ativo else 'Desativado❌'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')
            
    @classmethod
    def listar_cardapio(cls):
        print(f'{"Nome".ljust(25)} | {"Preço".ljust(25)}')
        for prato in cls._cardapio:
            print(f'{prato._nome.ljust(25)} | {prato._preco.ljust(25)}')      
    
    def alternar_status(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        if nota > 5:
            nota = nota / 2
        elif nota < 0:
            nota = 0
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliação ainda'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media_das_notas = round(soma_das_notas / quantidade_notas, 1) #arredonda as casas decimais 'round(argumento, #casas)
        return media_das_notas

    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)
    
    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
 
                    
    

