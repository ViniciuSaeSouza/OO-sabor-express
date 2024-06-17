from modelos.cardapio.item_cardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho) -> None:
        super().__init__(nome, preco)
        self.tamanho = tamanho
    
    def __str__(self) -> str:
        return self._nome