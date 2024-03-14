class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

categoria = Restaurante.categoria

nome_do_restaurante = restaurante_praca.nome
print(f'O restaunte {nome_do_restaurante} está ativo: {restaurante_praca.ativo}')

restaurante_sushi = Restaurante()

restaurantes = [restaurante_praca,restaurante_sushi]

# print(vars(restaurantes))