# Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.

dict_informacoes_participantes = {}

print(
    "\nInforme o nome e o conjunto de dados do participante ou digite 'sair' para encerrar a operação."
)
while True:
    nome_participante = (
        input("\nInforme o nome do participante do Workshop: ").title().strip()
    )

    if nome_participante == "Sair":
        break

    infos_participante = [
        dado.strip()
        for dado in input(
            "Informe os dados do participante(idade, estado civil, formação(separados por vírgula)): "
        )
        .title()
        .split(",")
    ]

    dict_informacoes_participantes[nome_participante] = infos_participante

print("\n=== Participantes do Workshop ===\n")
if len(dict_informacoes_participantes) == 0:
    print("Nenhum participante foi cadastrado.")
else:
    for nome, dados in dict_informacoes_participantes.items():
        print(
            f". Nome: {nome} - Dados(idade, estado civil, formação): {', '.join(dados)}."
        )
