class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self) -> str:
        return f'{self._nome} || {self._categoria} || {self._ativo}'
    
    def listar_restaurantes():
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')
            
    @property
    def ativo(self):
        return 'Ativo✅' if self._ativo else 'Desativado❌'
    
restaurante_praça = Restaurante('praça italiana', 'Gourmet')

restaurante_japa = Restaurante('seiji', 'Japonesa')

Restaurante.listar_restaurantes()
