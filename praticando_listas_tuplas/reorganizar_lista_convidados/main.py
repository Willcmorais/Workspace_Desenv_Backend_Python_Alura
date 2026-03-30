from gerenciador_lista import GerenciadorLista


def main():
    lista1 = GerenciadorLista()
    print(lista1)
    print()
    lista1.adicionar_convidado(0, "João")
    lista1.adicionar_convidado(2, "William")
    lista1.adicionar_convidado(5, "Pedro")
    print("--- Lista de convidados atualizada ---")
    lista1.mostrar_lista()


if __name__ == "__main__":
    main()
