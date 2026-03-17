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
            print("[Erro] Digite apenas números inteiros válidos.")
            limpar_tela()
            continue

        if not (1 <= numero_escolhido <= 100):
            print("[Atenção] Você precisa escolher um número entre 1 e 100.")
        elif numero_escolhido < numero_secreto:
            print("Você errou. Mas não desista, você está quase lá!")
            print("DICA: O número secreto É MAIOR...")
        elif numero_escolhido > numero_secreto:
            print("Você errou. Mas não desista, você está quase lá!")
            print("DICA: O número secreto é MENOR...")
        else:
            print(f"\n🎉 Parabéns! Você acertou o número secreto ({numero_secreto}).")
            break
        limpar_tela()
