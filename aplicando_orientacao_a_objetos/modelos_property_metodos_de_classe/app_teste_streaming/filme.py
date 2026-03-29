class Filme:
    def __init__(self, titulo, categoria, diretor, duracao):
        self._titulo = titulo.title()
        self._categoria = categoria.title()
        self._diretor = diretor.title()
        self._duracao = duracao

    def __str__(self):
        return f"{self._titulo.ljust(25)} | {self._categoria.ljust(25)} | {self._diretor.ljust(25)} | {self._duracao}"
