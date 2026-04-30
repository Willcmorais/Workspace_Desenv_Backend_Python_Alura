# Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

produtos = {}

print(
    "\nInforme o nome e a quantidade de produtos. Digite 'sair' para parar a operação."
)

while True:
    print()
    entrada_produto = input("Digite o nome do produto: ").title()

    if entrada_produto == "Sair":
        break

    entrada_qntd = input("Digite a quantidade: ")

    produtos[entrada_produto] = entrada_qntd

print("\n=== Produtos Cadastrados no Estoque ===\n")
if len(produtos) == 0:
    print(". Nenhum produto cadastrado.")
else:
    for produto, qntd in produtos.items():
        print(f". Nome: {produto} - Quantidade: {qntd}")

# Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.

if len(produtos) != 0:
    produto_atualizado = input(
        "\nInforme o nome do produto que deseja atualizar no estoque: "
    ).title()

    if produto_atualizado in produtos:
        qntd_atualizado = input(
            "\nInforme a atualização da quantidade do produto no estoque: "
        )
        produtos[produto_atualizado] = qntd_atualizado
    else:
        print("\nO produto não existe no estoque.")
else:
    print("\nO estoque está vazio!.")

print("\n=== Produtos Cadastrados no Estoque(Atualizado) ===\n")
if len(produtos) == 0:
    print(". Nenhum produto cadastrado.")
else:
    for produto, qntd in produtos.items():
        print(f". Nome: {produto} - Quantidade: {qntd}")
