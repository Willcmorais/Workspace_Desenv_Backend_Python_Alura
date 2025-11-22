# Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço. Crie um programa que junte as listas e exiba o resultado no formato produto: preço


def juntar_listas():
    nome = input("Informe o nome do produto: ").split(",")
    valor = input("Informe o valor do produto: ").split(",")
    nome_valor = list(zip(nome, valor))
    print(nome_valor)

    for nome, valor in nome_valor:
        print(f"{nome.strip()}: {valor.strip()}")

    return nome_valor


def main():
    juntar_listas()


if __name__ == "__main__":
    main()
