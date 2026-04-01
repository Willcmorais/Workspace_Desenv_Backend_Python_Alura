from gerenciador_lista import GerenciadorLista


def main():
    lista_convidados1 = GerenciadorLista()

    entrada = (
        input("Informe o nome dos convidados(separados por vígula): ")
        .title()
        .split(",")
    )
    lista_convidados1.adicionar_convidados(entrada)
    print()

    lista_convidados1.mostrar_lista()
    print()

    novo_convidado = input("Informe o nome do novo convidado: ")
    posicao = int(input("Informe a posição do novo convidado na lista: "))

    lista_convidados1.remanejar_novo_convidado(posicao, novo_convidado)
    print()

    lista_convidados1.mostrar_lista()


if __name__ == "__main__":
    main()
