from estoque import Estoque


def main():

    estoque1 = Estoque("Estoque do José")
    estoque1.adicionar_ao_estoque()
    print()
    estoque1.listar_estoque()
    print()
    estoque2 = Estoque("Estoque da Mariana")
    estoque2.adicionar_ao_estoque()
    print()
    estoque2.listar_estoque()
    print()
    estoque_geral = Estoque("Estoque Geral")
    estoque_geral.listar_estoque_geral()


if __name__ == "__main__":
    main()
