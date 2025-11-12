# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.

# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.


def aprovar_emprestimo():
    """
    Esta função vai informar se um empréstimo é aceito ou não. O empréstimo só será aprovado caso o usuário tenha uma renda mensal superior à R$2.000,00 e o valor do empréstimo não ultrapasse 30% da sua renda.

    Inputs:
    - Valor da renda mensal;
    - Valor da parcela desejada para emrpréstimo.

    Outputs:
    - Condicional se o empréstimo foi aprovado, de acordo com as informações fornecidas pelo usuário;
    - Mensagem se o empréstimo foi aprovado ou recusado.
    """

    valor_renda_mensal = float(input("Informe a sua renda mensal(R$): "))
    valor_parcela = float(input("Informe o valor da parcela desejada(R$): "))

    emprestimo_aprovado = valor_renda_mensal > 2000 and valor_parcela <= (
        valor_renda_mensal * 0.3
    )

    if emprestimo_aprovado:
        print(
            f"Parabéns Pedro, seu empréstimo de R${valor_parcela} foi aprovado com sucesso!"
        )
    else:
        print(
            f"Pedro, infelizmente seu empréstimo de R${valor_parcela} não foi aprovado."
        )


def main():
    aprovar_emprestimo()


if __name__ == "__main__":
    main()
