from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
import os

restaurante_charles = Restaurante('Charles Pizzaria', 'Pizzaria')

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande', 'Bebida')
bebida_suco.aplicar_desconto()

prato_pizza = Prato ('Pizza top', 12.00, 'Pizza de catupiru', 'Prato')
prato_pizza.aplicar_desconto()

sobremesa_pudim = Sobremesa ('Pudim', 12, 'Médio', 'Sobremesa')
sobremesa_pudim.aplicar_desconto()

restaurante_charles.adicionar_no_cardapio(bebida_suco)
restaurante_charles.adicionar_no_cardapio(prato_pizza)
restaurante_charles.adicionar_no_cardapio(sobremesa_pudim)



def main():
    os.system('cls')
    print(bebida_suco)
    print(prato_pizza)
    restaurante_charles.exibir_cardapio
    


if __name__ == '__main__':
    main()