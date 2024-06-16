class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)
        
    def __str__(self) -> str:
        return f"Título: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao} | Disponível: {self.disponivel}"
    
    @property
    def disponivel(self):
        return 'Disponível ✔' if self._disponivel else 'Indisponível ✖'
    
    def emprestar_livro(self):
        self._disponivel = False
    
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
    

        