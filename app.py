from modelos.restaurante import Restaurante
import os

restaurante_japa = Restaurante('seiji', 'Japonesa')

restaurante_japa.receber_avaliacao('Saes', 10)
restaurante_japa.receber_avaliacao('Elcio', 7)



def main():
    os.system('cls')
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()