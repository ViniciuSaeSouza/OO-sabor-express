from modelos.cardapio.item_cardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho, tipo) -> None:
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._tipo = tipo
    
    def __str__(self) -> str:
        return self._nome
    
    def aplicar_desconto(self): #Aplica desconto de 5%
        self._preco *= 0.95