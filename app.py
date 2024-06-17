from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
import os

restaurante_charles = Restaurante('Charles Pizzaria', 'Pizzaria')

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
prato_pizza = Prato ('Pizza top', 12.00, 'Pizza de catupiru')

restaurante_charles.adicionar_no_cardapio(bebida_suco)
restaurante_charles.adicionar_no_cardapio(prato_pizza)



def main():
    os.system('cls')
    print(bebida_suco)
    print(prato_pizza)
    restaurante_charles.exibir_cardapio
    


if __name__ == '__main__':
    main()