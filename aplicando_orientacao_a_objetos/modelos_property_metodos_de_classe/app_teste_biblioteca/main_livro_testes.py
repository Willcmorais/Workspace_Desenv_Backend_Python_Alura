from livro_testes import Livro
from biblioteca_testes import Biblioteca


def main():
    # Criando a Biblioteca
    minha_biblioteca = Biblioteca("Biblioteca Central")

    # Criando os livros
    livro1 = Livro("intuição", "osho", 2003)
    livro2 = Livro("código limpo", "robert c. martin", 2009)
    livro3 = Livro("o seminarista", "rubem fonseca", 2009)
    livro4 = Livro("cidade de vidro", "cassandra clare", 2009)

    # Adicionando os livros à biblioteca
    minha_biblioteca.adicionar_livro(livro1)
    minha_biblioteca.adicionar_livro(livro2)
    minha_biblioteca.adicionar_livro(livro3)
    minha_biblioteca.adicionar_livro(livro4)

    # Emprestando livros
    livro2.emprestar()
    livro4.emprestar()

    # Listando todos
    minha_biblioteca.listar_livros()
    print()  # Pula uma linha

    # Usando o filtro
    ano_busca = int(input("Informe o ano de publicação para buscar: "))
    encontrados = minha_biblioteca.filtrar_por_ano(ano_busca)

    print(f"\n----- Livros encontrados de {ano_busca} -----")
    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado para este ano.")


if __name__ == "__main__":
    main()
