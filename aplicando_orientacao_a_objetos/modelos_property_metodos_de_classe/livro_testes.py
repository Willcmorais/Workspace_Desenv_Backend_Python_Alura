class Livro:
    livros_catalogados = []

    def __init__(self, titulo="", autor="", ano_publicacao=0):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros_catalogados.append(self)

    def __str__(self):
        return f"{self._titulo} | {self._autor} | {self._ano_publicacao} | {self.disponivel}"

    @classmethod
    def filtrar_titulos(cls):
        filtro_ano_publicacao = int(input("Informe o ano de publicação: "))

        # Compreensão de listas é o laço for em uma linha(o que quero guardar | de onde estou tirando | qual a condição). Lemos: "guarde a variável livro em uma nova lista para cada livro encontrado dentro da lista de todos os livros. Mas, apenas se o ano do livro na lista geral for igual ao ano do livro informado no input do filtro."
        livros_filtrados = [
            livro
            for livro in cls.livros_catalogados
            if livro._ano_publicacao == filtro_ano_publicacao
        ]
        return livros_filtrados

    @property
    def disponivel(self):
        return "Disponível" if self._disponivel else "Indisponível"

    def emprestar(self):
        self._disponivel = not self._disponivel
        return self._disponivel
