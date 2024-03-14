class Filme:
    nome = ''
    ano_de_lancamento = int
    nota_do_filme = float

filme_Hancock = Filme()
filme_Hancock.nome = 'Hancock'
filme_Hancock.ano_de_lancamento = 2011
filme_Hancock.nota_do_filme = 8.6

print(vars(filme_Hancock))