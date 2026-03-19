import os


# ====== Funções auxiliares ======
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


# ====== Funções de lógica principais ======
def adicionar_tarefa(lista: list) -> None:
    tarefa = input("Informe qual tarefa deseja adicionar: ").capitalize()
    lista.append(tarefa)


def listar_tarefas(lista: list) -> None:
    print("\n--- Suas Tarefas ---")
    for tarefa in lista:
        print(tarefa)
    pass


def eliminar_tarefa(lista: list) -> None:
    print("\n--- Remover Tarefa ---")
    # Lógica para remover virá aqui...
    pass


def executar_opcao_escolhida(opcao: str, lista: list) -> bool:
    match opcao:
        case "1":
            adicionar_tarefa(lista)
            print("Tarefa adicionada a lista com sucesso!")
            limpar_tela()
            return True  # Continua rodando
        case "2":
            listar_tarefas(lista)
            limpar_tela()
            return True
        case "3":
            eliminar_tarefa(lista)
            print("Tarefa removida da lista com sucesso!")
            limpar_tela()
            return True
        case "4":
            print("Saindo do gerenciador de tarefas... Até mais!")
            return False  # Encerra o loop principal


def obter_opcao() -> str:
    opcoes_validas = ("1", "2", "3", "4")
    while True:
        mostrar_menu()
        opcao_escolhida = input("\nEscolha uma das opções: ")

        if opcao_escolhida not in opcoes_validas:
            print("Digite uma opção válida.")
            limpar_tela()
            continue
        return opcao_escolhida


# ====== Função principal ======
def main():
    lista_de_tarefas = []
    rodando = True

    while rodando:
        limpar_tela()
        opcao = obter_opcao()
        rodando = executar_opcao_escolhida(opcao, lista_de_tarefas)
