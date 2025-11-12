# Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.


def num_par_ou_impar():
    """
    Esta função vai definir se um número inteiro informado é par ou impar, validado pela operação de resto da divisão. Se o número informado divido por dois tiver o resto da divisão igual a zero ele será par, se não, será impar.

    Inputs:
    - Número inteiro

    Outputs:
    - Resto da divisão do número informado por dois;
    - Informação se ele é par ou impar.
    """

    num = int(input("Informe um número inteiro: "))

    num_par = num % 2 == 0

    if num_par:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é impar.")


def main():
    num_par_ou_impar()


if __name__ == "__main__":
    main()
