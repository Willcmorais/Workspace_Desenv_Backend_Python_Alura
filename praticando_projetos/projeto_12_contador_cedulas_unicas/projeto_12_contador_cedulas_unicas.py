import os

# As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.
# Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor.
# O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.


def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu() -> None:
    limpar_tela()
    print("**** BEM VINDO AO ATM ****")
    print("Cédulas disponíveis para saque:\n")
    print(". R$ 2,00\n. R$ 5,00\n. R$ 10,00\n. R$ 50,00\n. R$ 100,00\n")


def solicitar_saque() -> int:
    saques_indisponiveis = [0, 1, 3]
    ultimo_digito = ["1", "3"]

    while True:
        try:
            # Solicita o valor ao usuário
            saque_solicitado = int(input("Informe o valor do saque: "))
            saque_solicitado_str = str(saque_solicitado)
            saque_solicitado_str = list(saque_solicitado_str)

            # Se o saque for menor ou igual a zero continua
            if saque_solicitado in saques_indisponiveis:
                print(
                    "Não temos saques disponíveis para R$ 0.00, R$ 1.00 e R$ 3.00. Informe um valor diferente.\n"
                )
                continue
            elif saque_solicitado_str[-1] in ultimo_digito:
                print(
                    "Impossível sacar valores finalizados em 1 e 3. Tente outro valor.\n"
                )
                continue

        except ValueError:
            print("Digite apenas números inteiros.\n")
            continue

        return saque_solicitado


def contar_notas(saque_solicitado: int) -> dict:
    cedulas_disponiveis = [100, 50, 20, 10, 5, 2]
    cedulas_selecionadas = {}

    for cedula in cedulas_disponiveis:
        # Quantas notas desse valor cabem no montante restante?
        qntd_de_notas = saque_solicitado // cedula

        if qntd_de_notas > 0:
            cedulas_selecionadas[cedula] = qntd_de_notas

            # Atualizamos o valor restante pegando apenas o "resto" da divisão
            saque_solicitado = saque_solicitado % cedula

    return cedulas_selecionadas


def main():
    mostrar_menu()

    saque_solicitado = solicitar_saque()

    notas_selecionadas = contar_notas(saque_solicitado)

    limpar_tela()

    print(
        f"Seu saque de R$ {saque_solicitado:.2f} já está sendo processado...\n\nVocê vai receber:\n"
    )

    for cedula, qntd_notas in notas_selecionadas.items():
        print(f"-> {qntd_notas} nota(s) de R$ {cedula:.2f}")

    print("\nAgradecemos a preferência. Volte sempre!")
