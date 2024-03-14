import os
os.system('cls')

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_seiji = Restaurante('Seiji', 'Japonesa')

restaurantes = [restaurante_praca,restaurante_seiji]

print(f"""
{restaurante_praca} 
{restaurante_seiji}
    """)

# print(restaurantes)