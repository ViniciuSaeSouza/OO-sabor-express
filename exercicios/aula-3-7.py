import os
os.system('cls')

class ContaBancaria:
    def __init__(self, titular='', saldo=0) -> None:
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    def __str__(self) -> str:
        return f'Titular: {self.titular} | Saldo: {self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        if conta._ativo:
            print('Sua conta já está ativa!')
        else:
            conta._ativo = True
    
conta01 = ContaBancaria('Saes', 5000)
conta02 = ContaBancaria('Souza', 2000)

print(conta01, conta02)

print(conta01._ativo)

conta01.ativar_conta(conta01)

print(conta01._titular)