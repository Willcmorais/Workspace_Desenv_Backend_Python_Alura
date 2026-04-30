# Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. Agora, ele precisa de um programa que apresente três informações:

# Os nomes de todos os participantes.
# As idades de todos os participantes.
# Uma relação completa com o nome e a idade de cada um.

# Sua tarefa é criar esse programa com base nas informações fornecidas.

infos_participantes = {}

print(
    "\nInforme o nome e a idade dos participantes abaixo ou digite 'sair' para parar a execução."
)
while True:
    nome_participante = input("\nInforme o nome do participante: ").title()
    if nome_participante == "Sair":
        break

    idade_participante = input(
        f"Informe a idade do participante({nome_participante}): "
    )

    infos_participantes[nome_participante] = idade_participante

if len(infos_participantes) == 0:
    print("\nNenhum participante foi adicionado.")
else:
    print(f"\nNomes dos Participantes: {', '.join(infos_participantes.keys())}.")
    print(f"\nIdades dos Participantes: {', '.join(infos_participantes.values())}.")

    print("\n=== Informações Gerais dos Participantes ===\n")
    for nome, idade in infos_participantes.items():
        print(f". Nome: {nome} - Idade: {idade}.")
