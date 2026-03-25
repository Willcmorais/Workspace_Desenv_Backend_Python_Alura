from livro_testes import Livro


class Biblioteca:
    def __init__(self, nome_biblioteca):
        self._nome_biblioteca = nome_biblioteca
        self._livros_catalogados = []

    def adicionar_livro(self, livro):
        self._livros_catalogados.append(livro)

    def listar_livros(self):
        print(f"--- Catálogo da Biblioteca: {self._nome_biblioteca} ---")
        for livro in self._livros_catalogados:
            print(livro)

    def filtrar_por_ano(self, ano):
        # Compreensão de listas é o laço for em uma linha(o que quero guardar | de onde estou tirando | qual a condição). Lemos: "guarde a variável livro em uma nova lista para cada livro encontrado dentro da lista de todos os livros. Mas, apenas se o ano do livro na lista geral for igual ao ano do livro informado no input do filtro."
        livros_filtrados = [
            livro for livro in self._livros_catalogados if livro._ano_publicacao == ano
        ]
        return livros_filtrados
