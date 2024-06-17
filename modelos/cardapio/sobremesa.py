from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tamanho, tipo) -> None:
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._tipo = tipo
    
    def __str__(self) -> str:
        return f'Nome: {self._nome} | Preço: {self._preco} | Tamanho: {self._tamanho} | Tipo: {self._tipo}'
    
    def aplicar_desconto(self): #aplica desconto de 10%
        self._preco *= 0.90