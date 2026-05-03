# Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. Sua tarefa é criar um programa que exiba o total de vendas por categoria.

vendas = {"Eletrônicos": [], "Eletrodomésticos": [], "Livros": []}

print("\n==== Cadastro Vendas de Produtos ====")
while True:
    categoria_produto = input(
        "\nInforme a categoria do produto para cadastro ou digite 'sair' para parar a operação: "
    ).title()

    if categoria_produto == "Sair":
        break

    if categoria_produto not in vendas:
        print("Informe uma categoria válida do catálogo.\n")
        continue

    nome_produto = input("Informe o nome do produto: ").title()
    qntd_vendas_produto = int(input("Informe a quantidade de vendas desse produto: "))
    valor_unit_produto = float(input("Informe o valor unitário do produto: "))

    vendas[categoria_produto].append(
        {
            "produto": nome_produto,
            "qnt_vendas": qntd_vendas_produto,
            "valor_unitario": valor_unit_produto,
        }
    )

print("\n==== Relatório de Vendas por Categoria ====\n")
for categoria, lista_produtos in vendas.items():
    print(f"--- CATEGORIA: {categoria} ---\n")

    vendas_total_categoria = 0

    if not lista_produtos:
        print("Não há produtos cadastrados nesta categoria.")

    else:
        for item in lista_produtos:
            subtotal = item["qnt_vendas"] * item["valor_unitario"]
            vendas_total_categoria += subtotal

            print(f"Produto: {item['produto']}")
            print(
                f"  Unidades vendidas: {item['qnt_vendas']} | Valor unitário: R$ {item['valor_unitario']:.2f}"
            )
            print(f"  Subtotal: R$ {subtotal:.2f}")
            print("-" * 20)

    print("-" * 20)
    print(f"TOTAL DA CATEGORIA {categoria.upper()}: R$ {vendas_total_categoria:.2f}")
    print("=" * 30, "\n")
