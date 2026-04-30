# Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.

print()
lista_tarefas_equipe1 = set(
    tarefa.strip()
    for tarefa in input(
        "Informe a lista de tarefas da equipe 1(separadas por vírgula): "
    )
    .title()
    .split(",")
)

lista_tarefas_equipe2 = set(
    tarefa.strip()
    for tarefa in input(
        "\nInforme a lista de tarefas da equipe 2(separadas por vírgula): "
    )
    .title()
    .split(",")
)

lista_unificada = lista_tarefas_equipe1.union(lista_tarefas_equipe2)

print("\nLista Geral de Tarefas:")
for indice, tarefa in enumerate(lista_unificada, 1):
    print(f".{indice} - {tarefa}")

tarefa_retirada = input("\nInforme a tarefa que deseja retirar da lista: ").title()

lista_unificada.remove(tarefa_retirada)

print("\nLista Geral de Tarefas(Atualizada):")
for indice, tarefa in enumerate(lista_unificada, 1):
    print(f".{indice} - {tarefa}")
