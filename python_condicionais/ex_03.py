# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.


def controle_de_temperatura():
    """
    Esta função vai controlar a temperatura de uma sala. Se for maior do que 25ºc vai emitir um alerta de temperatura acima da média esperada, se não, vai apenas informar que está tudo dentro do esperado.

    Inputs:
    - Temperatura da sala.

    Outputs:
    - Alertas de mensagens.
    """

    temperatura_sala = float(input("Informe a temperatura atual da sala: "))

    print(
        f"A temperatura atual da sala é de {temperatura_sala}ºc. Está dentro do esperado."
    ) if temperatura_sala <= 25 else print(
        f"ALERTA! A temperatura da sala é de {temperatura_sala}ºc. Está acima do suportado."
    )


def main():
    controle_de_temperatura()


if __name__ == "__main__":
    main()
