import random, os


def limpar_tela():
    # O próprio input já serve para pausar e esperar o Enter
    input("\nPressione 'Enter' para continuar...")
    # Condição para funcionar no Windows ('nt') ou Linux/Mac ('posix')
    os.system("cls" if os.name == "nt" else "clear")


def jogar():
    # Dicionário para traduzir o número na jogada correspondente
    opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

    # Variáveis de estado do jogo
    jogando = True
    pontos_jogador = 0
    pontos_maquina = 0

    while jogando:
        # Exibição do Placar
        print("=" * 35)
        print(f"  PLACAR: Você {pontos_jogador} x {pontos_maquina} Máquina")
        print("=" * 35)
        print("Opções: [1] Pedra | [2] Papel | [3] Tesoura | [0] Sair\n")

        # Validação de entrada
        try:
            opcao_escolhida = int(input("Informe sua jogada: "))
        except ValueError:
            print("Opção inválida! Por favor, pressione apenas números.")
            limpar_tela()
            continue

        # Condição de parada
        if opcao_escolhida == 0:
            print(
                f"\nSaindo do jogo... Placar final: Você {pontos_jogador} x {pontos_maquina} Máquina. Até mais!"
            )
            break

        # Validação de Opção Existente
        if opcao_escolhida not in opcoes:
            print("\nOpção inválida! Escolha 1, 2, 3 ou 0.")
            limpar_tela()
            continue

        opcao_da_maquina = random.randint(1, 3)

        # Agora mostramos o nome da jogada em vez do número
        print(
            f"\nVocê escolheu {opcoes[opcao_escolhida]} e máquina escolheu {opcoes[opcao_da_maquina]}."
        )

        # Verifica empate logo de cara para não precisar repetir a lógica
        if opcao_escolhida == opcao_da_maquina:
            print("Foi empate! Ninguém pontua.")
        else:
            match opcao_escolhida:
                case 1:
                    if opcao_da_maquina == 2:
                        print("A máquina cobriu sua pedra. Você perdeu!")
                        pontos_maquina += 1
                    else:
                        print("Sua pedra quebrou a tesoura. Você venceu!")
                        pontos_jogador += 1
                case 2:
                    if opcao_da_maquina == 3:
                        print("A tesoura cortou seu papel. Você perdeu!")
                        pontos_maquina += 1
                    else:
                        print("Seu papel cobriu a pedra. Você venceu!")
                        pontos_jogador += 1
                case 3:
                    if opcao_da_maquina == 1:
                        print("A pedra quebrou sua tesoura. Você perdeu!")
                        pontos_maquina += 1
                    else:
                        print("Sua tesoura cortou o papel. Você venceu!")
                        pontos_jogador += 1
        limpar_tela()
