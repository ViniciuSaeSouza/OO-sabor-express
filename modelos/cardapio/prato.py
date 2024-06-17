from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo) -> None:
        super().__init__(nome, preco)
        self._descricao = descricao
        self._tipo = tipo
        
    def __str__(self) -> str:
        return f'Nome: {self._nome} | Preço: {self._preco} | Descrição: {self._descricao} | Tipo: {self._tipo}'
    
    def aplicar_desconto(self): #Aplica desconto de 8%
        self._preco *= 0.92