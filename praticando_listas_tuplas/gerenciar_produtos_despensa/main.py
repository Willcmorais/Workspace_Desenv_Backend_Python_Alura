from gerenciador_despensa import Despensa


def main():
    despensa_roberto = Despensa("despensa roberto - casa de praia maracaípe")
    print()
    despensa_roberto.adicionar_produto_despensa()
    print()
    despensa_roberto.mostrar_despensa()
    print()
    despensa_roberto.verificar_produto()
    print()

    despensa_mario = Despensa("despensa mário - casa boa viagem")
    despensa_mario.adicionar_produto_despensa()
    print()
    despensa_mario.mostrar_despensa()
    print()
    despensa_mario.verificar_produto()


if __name__ == "__main__":
    main()
