from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao) -> None:
        super().__init__(nome, preco)
        self.descricao = descricao
        
    def __str__(self) -> str:
        return self._nome
        