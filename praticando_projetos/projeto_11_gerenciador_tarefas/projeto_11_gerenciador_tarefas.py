import os

# Menu interativo que permita adicionar, visualizar e remover tarefas de uma lista.


def limpar_tela() -> None:
    input("\nPressione 'Enter' para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    print("   GERENCIADOR DE TAREFAS")
    print("=" * 30)
    print("            MENU")
    print("=" * 30)
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")
    print("=" * 30)


def adicionar_tarefa() -> list:
    lista_de_tarefas = []

    tarefa = input("Informe qual tarefa deseja adicionar: ")

    lista_de_tarefas.append(tarefa)

    return lista_de_tarefas


def listar_tarefas(lista_de_tarefas) -> list:
    lista_de_tarefas = adicionar_tarefa
    print(lista_de_tarefas)


def obter_opcao() -> str:
    opcoes_validas = ("1", "2", "3", "4")

    while True:
        mostrar_menu()

        opcao_escolhida = input("\nEscolha uma das opções: ")

        if opcao_escolhida not in opcoes_validas:
            print("Digite uma opção válida.")
            limpar_tela()
            continue
        break

    match opcao_escolhida:
        case "1":
            adicionar_tarefa()
        case "2":
            listar_tarefas()
        case "3":
            ...
        case "4":
            ...
