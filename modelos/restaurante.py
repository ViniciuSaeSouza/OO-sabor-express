import os
os.system('cls')

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'    
    
restaurante_seiji = Restaurante('Seiji Sushi', 'Japonesa')


restaurante_nina = Restaurante("Nina's", 'Gourmet')

print(restaurante_seiji)
