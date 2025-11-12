# Você está desenvolvendo um sistema de controle de estoque para o Buscante. Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote. Sempre que uma venda é realizada, o sistema deve informar o usuário e atualizar a quantidade disponível.

# Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".


def controle_de_estoque():
    estoque_livro = 5

    for livro in range(estoque_livro - 1, -1, -1):
        print(f"Venda realizada! Estoque restante: {livro}")


def main():
    controle_de_estoque()


if __name__ == "__main__":
    main()
