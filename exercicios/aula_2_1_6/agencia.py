from exercicios.aula_2_1_6.banco import Banco

class Agencia(banco):
    def __init__(self, nome, endereco, numero) -> None:
        super().__init__(nome, endereco)
        self.numero = numero