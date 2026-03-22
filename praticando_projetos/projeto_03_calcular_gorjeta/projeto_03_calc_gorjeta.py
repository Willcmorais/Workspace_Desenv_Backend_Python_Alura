def mostrar_menu():
    print("*" * 30)
    print("=== CALCULADOR DE GORJETA ===")
    print("*" * 30)


def solicitar_informacoes():
    valor_da_conta = float(input("Informe o valor da conta do cliente(R$): "))
    porcentagem_da_gorjeta = float(input("Informe a porcentagem da gorjeta(%): "))

    valor_da_gorjeta, valor_total_a_pagar = calcular_gorjeta(
        porcentagem_da_gorjeta, valor_da_conta
    )

    print(
        f"\nO valor da gorjeta foi de R$ {valor_da_gorjeta:.2f}.\nO valor total da conta foi de R$ {valor_total_a_pagar:.2f}."
    )


def calcular_gorjeta(porcentagem_da_gorjeta, valor_da_conta):
    valor_da_gorjeta = valor_da_conta * (porcentagem_da_gorjeta) / 100
    valor_total_a_pagar = valor_da_conta + valor_da_gorjeta

    return valor_da_gorjeta, valor_total_a_pagar


def main():
    mostrar_menu()
    solicitar_informacoes()
