from carro import Carro
from moto import Moto
import os

carro = Carro('Hyundai', 'Hb20', 4)
moto = Moto('Honda', 'Hayabusa', 'Esportiva')

def main():
    os.system('cls')
    print(carro)
    print(moto)

if __name__ == '__main__':
    main()