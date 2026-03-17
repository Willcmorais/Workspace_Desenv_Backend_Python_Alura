import random, os

# ---------------------------------------------------------
# FUNÇÕES DE INTERFACE / VISUAIS
# ---------------------------------------------------------


def limpar_tela():
    # O próprio input já serve para pausar e esperar o Enter
    input("\nPressione 'Enter' para continuar...")
    # Condição para funcionar no Windows ('nt') ou Linux/Mac ('posix')
    os.system("cls" if os.name == "nt" else "clear")


def exibir_placar(pontos_jogador, pontos_maquina):
    # Exibição do Placar
    print("=" * 35)
    print(f"  PLACAR: Você {pontos_jogador} x {pontos_maquina} Máquina")
    print("=" * 35)
    print("Opções: [1] Pedra | [2] Papel | [3] Tesoura | [0] Sair\n")


# ---------------------------------------------------------
# FUNÇÕES DE LÓGICA / VALIDAÇÃO
# ---------------------------------------------------------


def validar_jogada(opcoes):
    while True:
        try:
            jogada = int(input("Informe a sua jogada: "))

            # Se a jogada for 0 ou uma das chaves do dicionário (1, 2, 3), é válida.
            if jogada == 0 or jogada in opcoes:
                # O return encerra a função e quebra o loop automaticamente
                return jogada

            # Se chegou aqui, é porque é um número, mas não é 0, 1, 2 ou 3
            print("\nOpção inválida! Escolha 1, 2, 3 ou 0 para sair.\n")

        except ValueError:
            # Se chegou aqui, é porque o usuário deu Enter vazio ou digitou letras
            print("\nEntrada inválida! Por favor, digite apenas números.\n")


def determinar_resultado(opcao_escolhida, opcao_da_maquina):
    # Verifica empate logo de cara para não precisar repetir a lógica
    if opcao_escolhida == opcao_da_maquina:
        return "empate", "Foi empate! Ninguém pontua."
    else:
        match opcao_escolhida:
            case 1:
                if opcao_da_maquina == 2:
                    return "maquina", "A máquina cobriu sua pedra. Você perdeu!"
                else:
                    return "jogador", "Sua pedra quebrou a tesoura. Você venceu!"

            case 2:
                if opcao_da_maquina == 3:
                    return "maquina", "A tesoura cortou seu papel. Você perdeu!"
                else:
                    return "jogador", "Seu papel cobriu a pedra. Você venceu!"

            case 3:
                if opcao_da_maquina == 1:
                    return "maquina", "A pedra quebrou sua tesoura. Você perdeu!"
                else:
                    return "jogador", "Sua tesoura cortou o papel. Você venceu!"


# ---------------------------------------------------------
# FUNÇÃO PRINCIPAL (CONTROLADOR)
# ---------------------------------------------------------


def jogar():
    # Dicionário para traduzir o número na jogada correspondente
    opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

    # Variáveis de pontuação
    pontos_jogador = 0
    pontos_maquina = 0

    # Variáveis de estado do jogo
    jogando = True

    while jogando:
        # Chama a função para mostrar o placar
        exibir_placar(pontos_jogador, pontos_maquina)

        # Função que valida a jogada
        opcao_escolhida = validar_jogada(opcoes)

        # Condição de parada
        if opcao_escolhida == 0:
            print(
                f"\nSaindo do jogo... Placar final: Você {pontos_jogador} x {pontos_maquina} Máquina. Até mais!"
            )
            break

        opcao_da_maquina = random.randint(1, 3)

        # Agora mostramos o nome da jogada em vez do número
        print(
            f"\nVocê escolheu {opcoes[opcao_escolhida]} e máquina escolheu {opcoes[opcao_da_maquina]}."
        )

        # Função que determina os resultados
        resultado, mensagem = determinar_resultado(opcao_escolhida, opcao_da_maquina)

        print(mensagem)

        if resultado == "jogador":
            pontos_jogador += 1
        elif resultado == "maquina":
            pontos_maquina += 1

        limpar_tela()
