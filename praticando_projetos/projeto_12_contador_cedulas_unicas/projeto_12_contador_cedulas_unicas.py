import os

# As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.
# Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor.
# O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.


def limpar_tela() -> None:
    input("\nPressione 'Enter' para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    print("**** BEM VINDO AO CAIXA ELETRÔNICO ****")
    print("    Cédulas disponíveis para saque\n")


def solicitar_valor_de_saque(saque: float) -> float:
    cedulas_disponiveis = (
        2.0,
        5.0,
        10.0,
        20.0,
        50.0,
        100.0,
    )

    mostrar_menu()

    for cedula in cedulas_disponiveis:
        print(f". R$ {cedula}")

    while True:
        try:
            saque = float(input("\nInforme o valor que deseja sacar: "))

            if saque not in cedulas_disponiveis:
                print("Digite um valor de saque válido.")
                continue
        except ValueError:
            print("[Erro] Digite apenas dígitos númericos.")
            continue
        return


def contar_cedulas():
    pass


def main():

    saque = solicitar_valor_de_saque(saque=float)
    print(saque)
