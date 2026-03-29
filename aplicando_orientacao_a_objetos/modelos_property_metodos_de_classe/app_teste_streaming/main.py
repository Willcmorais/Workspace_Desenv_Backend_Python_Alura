from filme import Filme
from streaming import Streaming
from cliente import Cliente


def main():
    # ==========CLIENTES============
    cliente1 = Cliente("william", "william@gmail.com", "blablabla")
    cliente2 = Cliente("carlos", "carlos@gmail.com", "basic")

    # ============STREAMINGS===========
    streaming1 = Streaming("WillFlix")
    streaming2 = Streaming("VicFlix")

    # =============FILMES===============
    filme1 = Filme("o agente secreto", "mistério", "kleber mendonça filho", 158)
    filme2 = Filme("bugonia", "ficção/comedia sombria", "yorgos lanthimos", 119)
    filme3 = Filme(
        "tipos de gentileza", "ficção/comédia sombria", "yorgos lanthimos", 165
    )
    filme4 = Filme("pobres criaturas", "ficção/comédia ácida", "yorgos lanthimos", 161)

    # ===============TESTES================
    streaming1.adicionar_filme_catalogo(filme1)
    streaming1.adicionar_filme_catalogo(filme2)
    streaming2.adicionar_filme_catalogo(filme3)
    streaming2.adicionar_filme_catalogo(filme4)
    streaming1.mostrar_filmes_catalogados()
    print()
    streaming2.mostrar_filmes_catalogados()

    print(cliente2._plano)
    print(cliente1._plano)


if __name__ == "__main__":
    main()
