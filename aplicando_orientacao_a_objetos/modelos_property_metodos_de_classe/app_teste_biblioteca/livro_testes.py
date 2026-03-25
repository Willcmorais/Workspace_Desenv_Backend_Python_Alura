class Livro:
    # Removemos a lista livros_catalogados daqui!

    def __init__(self, titulo="", autor="", ano_publicacao=0):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        # Removemos o .append(self) daqui também!

    def __str__(self):
        return f"{self._titulo} | {self._autor} | {self._ano_publicacao} | {self.disponivel}"

    @property
    def disponivel(self):
        return "Disponível" if self._disponivel else "Indisponível"

    # Propriedade para acessar o ano facilmente na Biblioteca
    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    def emprestar(self):
        self._disponivel = not self._disponivel
        return self._disponivel
