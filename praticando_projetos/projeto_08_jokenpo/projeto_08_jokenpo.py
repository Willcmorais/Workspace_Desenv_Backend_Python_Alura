import random


def jogar():
    opcao_escolhida = int(input("Informe sua jogada: "))
    opcao_da_maquina = random.randint(1, 3)

    print(f"A máquina escolheu {opcao_da_maquina}")

    match opcao_escolhida:
        case 1:
            if opcao_da_maquina == 1:
                print("Foi empate!")
            elif opcao_da_maquina == 2:
                print("Você perdeu!")
            else:
                print("Você venceu!")
        case 2:
            if opcao_da_maquina == 1:
                print("Você venceu!")
            elif opcao_da_maquina == 2:
                print("Foi empate!")
            else:
                print("Você perdeu!")
        case 3:
            if opcao_da_maquina == 1:
                print("Você perdeu!")
            elif opcao_da_maquina == 2:
                print("Você venceu!")
            else:
                print("Foi empate!")
        case _:
            print("Opção inválida!")
