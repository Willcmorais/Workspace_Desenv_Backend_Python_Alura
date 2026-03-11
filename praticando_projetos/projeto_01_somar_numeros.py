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
            return print(f"Erro: Digite apenas números válidos!")
    return print(f"A soma dos valores foi {soma}")


somar_numeros()
# help(somar_numeros)
