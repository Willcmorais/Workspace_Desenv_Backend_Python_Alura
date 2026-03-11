def calcular_gorjeta(valor_da_conta, porcentagem_da_gorjeta):
    valor_da_gorjeta = valor_da_conta * (porcentagem_da_gorjeta) / 100
    valor_total_a_pagar = valor_da_conta + valor_da_gorjeta

    return print(
        f"Valor da gorjeta: R${valor_da_gorjeta:.2f}\nTotal a pagar: R${valor_total_a_pagar:.2f}"
    )
