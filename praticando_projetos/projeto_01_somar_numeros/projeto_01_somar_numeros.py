def somar_numeros():
    """
    A função faz a soma de dois números digitados pelo usuário.

    Inputs:
    - 2 valores em float.

    Outputs:
    - A soma dos valores.
    - Mensagem de erro caso não sejam digitados números válidos.
    """
    soma = 0

    for i in range(1, 3):
        try:
            numero = float(input(f"Informe o {i}º número: "))
            soma += numero
        except ValueError:
            return print("Erro: Digite apenas números válidos!")
    return soma


def main():
    soma_dos_numeros = somar_numeros()

    print(f"\nA soma dos números é igual a {soma_dos_numeros}.")
