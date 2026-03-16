import random, os, keyboard


def limpar_tela():
    print("Pressione 'Enter' para continuar...")
    keyboard.wait("enter")
    os.system("cls")


def jogar():
    jogar = True

    while jogar:
        opcao_escolhida = int(input("Informe sua jogada: "))
        opcao_da_maquina = random.randint(1, 3)

        print(f"A máquina escolheu {opcao_da_maquina}")

        match opcao_escolhida:
            case 1:
                if opcao_da_maquina == 1:
                    print("\nVocê escolheu pedra e a máquina também. Foi empate!\n")
                    limpar_tela()
                elif opcao_da_maquina == 2:
                    print("\nVocê escolheu pedra e a máquina Papel. Você perdeu!\n")
                    limpar_tela()
                else:
                    print("\nVocê escolheu pedra e a máquina tesoura. Você venceu!\n")
                    limpar_tela()
            case 2:
                if opcao_da_maquina == 1:
                    print("\nVocê escolheu papel e a máquina pedra. Você venceu!\n")
                    limpar_tela()
                elif opcao_da_maquina == 2:
                    print("\nVocê escolheu papel e a máquina também. Foi empate!\n")
                    limpar_tela()
                else:
                    print("\nVocê escolheu papel e a máquina tesoura. Você perdeu!\n")
                    limpar_tela()
            case 3:
                if opcao_da_maquina == 1:
                    print("\nVocê escolheu tesoura e a máquina pedra. Você perdeu!\n")
                    limpar_tela()
                elif opcao_da_maquina == 2:
                    print("\nVocê escolheu tesoura e a máquina papel. Você venceu!\n")
                    limpar_tela()
                else:
                    print("\nVocê escolheu tesoura e a máquina também. Foi empate!\n")
                    limpar_tela()
            case _:
                print("Opção inválida!")
                jogar = False
