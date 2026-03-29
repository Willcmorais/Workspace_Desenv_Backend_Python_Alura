from verificando_itens_dispensa import Despensa


def main():
    despensa_roberto = Despensa("despensa roberto - casa de praia maracaípe")
    despensa_roberto.mostrar_despensa()
    print()
    despensa_roberto.verificar_produto("brócolis")
    despensa_roberto.verificar_produto("feijão")
    print()

    despensa_mario = Despensa("despensa mário - casa boa viagem")
    despensa_mario.adicionar_produto_despensa("abacate")
    despensa_mario.mostrar_despensa()
    print()
    despensa_mario.verificar_produto("jiló")
    despensa_mario.verificar_produto("abacate")


if __name__ == "__main__":
    main()
