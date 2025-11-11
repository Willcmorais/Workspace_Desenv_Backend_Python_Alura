# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.


def calculo_de_despesas():
    """
    Esta função vai calcular despesas mensais do usuário. Tendo em vista o limite de R$3.000,00.

    Inputs:
    - Gasto mensal

    Outputs:
    - Informação se o gasto mensal ultrapassou o orçamento ou não.
    """

    gastos = float(input("Digite o total de despesas do mês(R$): "))

    limite_ultrapassado = gastos > 3000

    print(
        f"Seu gasto mensal foi de R${gastos}. Você ultrapassou o seu limite."
    ) if limite_ultrapassado else print(
        f"Seu gasto mensal foi de R${gastos}. Você não ultrapassou o seu limite."
    )


def main():
    calculo_de_despesas()


if __name__ == "__main__":
    main()
