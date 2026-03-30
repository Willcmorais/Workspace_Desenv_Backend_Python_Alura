from estoque import Estoque


def main():
    estoque = Estoque("Estoque do Armando")
    print(estoque)
    estoque.unificar_estoque()
    print()
    estoque.listar_estoque()


if __name__ == "__main__":
    main()
