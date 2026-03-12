from projeto_03_calc_gorjeta import calcular_gorjeta

valor_da_conta = float(input("Informe o valor da conta do cliente(R$): "))
porcentagem_da_gorjeta = float(input("Informe a porcentagem da gorjeta(%): "))

valor_total = calcular_gorjeta(valor_da_conta, porcentagem_da_gorjeta)
