from estoque import Estoque


def main():
    estoque1 = Estoque("Estoque do José")
    entrada_estoque1 = estoque1.solicitar_entrada()
    estoque1.adicionar_ao_estoque(entrada_estoque1)
    print()
    estoque1.listar_estoque()
    print()

    estoque2 = Estoque("Estoque da Mariana")
    entrada_estoque2 = estoque2.solicitar_entrada()
    estoque2.adicionar_ao_estoque(entrada_estoque2)
    print()
    estoque2.listar_estoque()
    print()

    estoque3 = Estoque("Estoque do João")
    entrada_estoque3 = estoque3.solicitar_entrada()
    estoque3.adicionar_ao_estoque(entrada_estoque3)
    print()
    estoque3.listar_estoque()
    print()
    estoque3.unificar_estoques(estoque1, estoque2)


if __name__ == "__main__":
    main()
