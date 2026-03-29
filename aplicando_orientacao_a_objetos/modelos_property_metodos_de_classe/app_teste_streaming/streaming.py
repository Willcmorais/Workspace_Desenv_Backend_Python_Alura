class Streaming:
    def __init__(self, nome):
        self._nome = nome.upper()
        self._catalogo_filmes = []

    def adicionar_filme_catalogo(self, filme):
        self._catalogo_filmes.append(filme)

    def mostrar_filmes_catalogados(self):
        print("=" * 44, f"{self._nome}", "=" * 44)
        print()
        print(
            f'{"Título:".ljust(25)} | {"Categoria:".ljust(25)} | {"Diretor:".ljust(25)} | {"Duração(min):"}'
        )
        for filme in self._catalogo_filmes:
            print(filme)
