from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._avaliacao = []
        self._ativo = False
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
            
    

