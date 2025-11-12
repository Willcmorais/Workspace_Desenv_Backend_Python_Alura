# Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.

# Ajude Ana a decidir entre usar um laço for ou while. Escreva o programa usando o laço que você acredita ser mais adequado para essa tarefa e explique por que escolheu esse laço.

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]


def mostrar_clientes():
    """
    Esta função vai percorrer todos os nomes de uma lista de clientes e mostrar esses nomes.

    Outputs:
    - Nomes dos clientes.
    """

    for nome in clientes:
        print(nome)


def main():
    mostrar_clientes()


if __name__ == "__main__":
    main()
