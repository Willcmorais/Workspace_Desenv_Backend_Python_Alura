# Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.


def liberacao_de_acesso():
    """
    Esta função vai informar se o acesso do usuário está liberado ou não de acordo com a hora atual. Se a hora estiver entre 08h e 18h ele tem o acesso liberado, se não, o acesso é negado.

    Inputs:
    - Horário atual

    Outputs:
    - Informação de acesso liberado ou negado.
    """
    horario_atual = int(input("Informe a hora atual(Formato de 24h): "))

    acesso_liberado = horario_atual >= 8 and horario_atual <= 18

    print("Acesso liberado!") if acesso_liberado else print("Acesso negado!")


def main():
    liberacao_de_acesso()


if __name__ == "__main__":
    main()
