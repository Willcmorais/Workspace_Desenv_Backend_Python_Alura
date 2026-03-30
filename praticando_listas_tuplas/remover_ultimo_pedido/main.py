# Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos os pedidos, mas percebeu que o último foi inserido por engano e precisa removê-lo. Diante deste problema, ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o último item automaticamente.


def main():
    lista_pedidos = [
        "Hamburguer",
        "Refrigerante",
        "Batata Frita",
        "Suco",
        "Cachorro Quente",
        "Sobremesa",
    ]

    print(f"Lista de pedidos original:\n{lista_pedidos}\n")

    print(f"{lista_pedidos.pop(-1)} retirado da lista\n")

    print(f"Lista de pedidos atualizada:\n{lista_pedidos}")


if __name__ == "__main__":
    main()
