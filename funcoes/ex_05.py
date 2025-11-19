import os

# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços. Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.


def somar_vendas_diarias(vendas_dia):
    return sum(vendas_dia)


def main():
    valor = input(
        "Informe a quantidade de vendas diárias(separado por espaços): "
    ).split()

    total_dias = list(map(lambda x: int(x), valor))

    os.system("cls")

    print(f"Listagem de vendas diárias: {total_dias}")
    print(f"Total em {len(total_dias)} dias: {somar_vendas_diarias(total_dias)} vendas")


if __name__ == "__main__":
    main()
