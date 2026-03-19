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
    tarefa = input("\nInforme qual tarefa deseja adicionar: ").strip().capitalize()
    lista.append(tarefa)
    print("Tarefa adicionada a lista com sucesso!")


def listar_tarefas(lista: list) -> None:
    print("\n--- Suas Tarefas ---")

    if not lista:
        print("Sua lista está vazia!")
        return

    # O enumerate(lista) gera pares: (0, "Tarefa A"), (1, "Tarefa B")...
    for indice, tarefa in enumerate(lista):
        print(f"{indice}. {tarefa}")


def eliminar_tarefa(lista: list) -> None:
    print("\n--- Remover Tarefa ---")

    if not lista:
        print("A lista está vazia!")
        limpar_tela()
        return

    while True:
        try:
            tarefa_removida = int(
                input("\nInforme o índice da tarefa que quer remover: ")
            )

            if tarefa_removida not in range(len(lista)) or tarefa_removida < 0:
                print("Informe um índice válido!")
                continue

            tarefa_apagada = lista.pop(tarefa_removida)
            print(f"Tarefa ({tarefa_apagada}) removida da lista com sucesso!")
            break

        except ValueError:
            print("[Erro] Por gentileza, digite apenas números inteiros.")


def executar_opcao_escolhida(opcao: str, lista: list) -> bool:
    match opcao:
        case "1":
            adicionar_tarefa(lista)
            limpar_tela()
            return True  # Continua rodando
        case "2":
            listar_tarefas(lista)
            limpar_tela()
            return True
        case "3":
            eliminar_tarefa(lista)
            limpar_tela()
            return True
        case "4":
            print("Saindo do gerenciador de tarefas... Até mais!")
            return False  # Encerra o loop principal


def obter_opcao() -> str:
    # define as tuplas válidas
    opcoes_validas = ("1", "2", "3", "4")
    # entra no loop
    while True:
        # vai para a função de mostrar o menu
        mostrar_menu()
        # volta para a função obter opção, pois é o que está na frente da pilha de execução
        opcao_escolhida = input("\nEscolha uma das opções: ")

        if opcao_escolhida not in opcoes_validas:
            print("Digite uma opção válida.")
            limpar_tela()
            continue
        return opcao_escolhida


# ====== Função principal ======
def main():
    # início de toda a execução
    lista_de_tarefas = []
    rodando = True

    while rodando:
        # para e vai para outra função
        opcao = obter_opcao()
        # após obter a opção ele volta para o main e executa a linha que vai pausar novamente e jogar para outra função
        rodando = executar_opcao_escolhida(opcao, lista_de_tarefas)
