# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda. Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.


def calcular_vendas_macas_bananas():
    """
    Esta função calcula a quantidade de vendas entre dois produtos.

    Inputs:
    - Vendas de maçãs;
    - Vendas de bananas.

    Outputs:
    - Mensagem comparativa entre a quantidade de vendas, se uma é maior, menor ou igual à outra.
    """

    vendas_macas = int(input("Informe a quantidade de vendas de maçãs: "))
    vendas_bananas = int(input("Informe a quantidade de vendas de bananas: "))

    if vendas_macas > vendas_bananas:
        print("Foram vendidas mais maçãs do que bananas.")
    elif vendas_bananas > vendas_macas:
        print("Foram vendidas mais bananas do que maçãs.")
    else:
        print("As vendas de bananas e maçãs foram iguais.")


def main():
    """
    Esta função vai chamar a função de calcular as vendas
    """
    calcular_vendas_macas_bananas()


if __name__ == "__main__":
    main()
