class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self) -> str:
        return f'{self.nome} || {self.categoria} || {self.ativo}'
        
    
restaurante_praça = Restaurante('Praça', 'Gourmet')

restaurante_japa = Restaurante('Seiji', 'Japonesa')

restaurantes = [restaurante_praça, restaurante_japa]

print(restaurante_praça)
print(restaurante_japa)