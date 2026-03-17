import random, os


def limpar_tela():
    input("\nPressione 'Enter' para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


def adivinhar_numero():
    numero_secreto = random.randint(1, 100)

    while True:
        print("--- JOGO DE ADIVINHAÇÃO ---")
        print("Adivinhe o número secreto entre 1 e 100.\n")

        try:
            numero_escolhido = int(input("Digite qual número acha que é o secreto: "))
        except ValueError:
            print("Digite apenas números inteiros válidos.")
            limpar_tela()
            continue

        if numero_escolhido not in range(1, 101):
            print("Você precisa escolher um número entre 1 e 100.")
            limpar_tela()
            continue
        if numero_escolhido < numero_secreto:
            print("Você errou. Mas não desista, você está quase lá!")
            print("O número que você escolheu é menor que o número secreto...")
            limpar_tela()
            continue
        if numero_escolhido > numero_secreto:
            print("Você errou. Mas não desista, você está quase lá!")
            print("O número que você escolheu é maior que o número secreto...")
            limpar_tela()
            continue
        else:
            print("Parabéns! Você acertou o número secreto.")
            break
