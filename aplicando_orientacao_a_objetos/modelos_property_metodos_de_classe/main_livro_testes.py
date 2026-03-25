from livro_testes import Livro

livro1 = Livro("intuição", "osho", 2003)
livro2 = Livro("código limpo", "robert c. martin", 2009)
livro3 = Livro("o seminarista", "rubem fonseca", 2009)
livro4 = Livro("cidade de vidro", "cassandra clare", 2009)

# livro1.emprestar
livro2.emprestar()


def main():
    print(livro1)
    print(livro2)
    print()

    livros_encontrados = Livro.filtrar_titulos()

    print("\n----- Livros encontrados -----")
    for livro in livros_encontrados:
        print(livro)


if __name__ == "__main__":
    main()
