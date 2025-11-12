# Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

# Até 100 km: R$ 10,00
# Entre 100 km e 200 km: R$ 20,00
# Acima de 200 km: R$ 30,00

# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.


def calculo_de_pedagio():
    """
    Esta função vai calcular o valor de um pedágio de acordo com a distância percorrida.

    Inputs:
    - Distância percorrida.

    - Outputs:
    - Valor da cobrança do pedágio.
    """
    distancia_percorrida = float(input("Informe a distância percorrida: "))

    pedagio_valor_10 = distancia_percorrida <= 100
    pedagio_valor_20 = 100 < distancia_percorrida <= 200

    if pedagio_valor_10:
        print(f"Valor do pedágio(R$): 10,00.")
    elif pedagio_valor_20:
        print(f"Valor do pedágio(R$): 20,00.")
    else:
        print(f"Valor do pedágio(R$): 30,00.")


def main():
    calculo_de_pedagio()


if __name__ == "__main__":
    main()
