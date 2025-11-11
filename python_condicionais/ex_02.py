# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total. Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.


def calculo_tempo_total_projeto():
    """
    Esta função vai receber a quantidade de dias para realizar 3 projetos. Caso a quantidade de dias seja maior ou igual a 0 ele vai somar os dias, caso contrário vai mostrar uma mensagem de erro e vai voltar para a pergunta até que seja inserido um número válido.

    Inputs:
    - Quantidade de dias

    Outputs:
    - Mensagem de erro caso seja inserido um dia negativo;
    - O tempo total de dias que foi calculado.
    """
    soma_dias = 0
    atividade = 1

    while atividade <= 3:
        dias = int(
            input(
                f"Informe a quantidade de dias para realizar a {atividade}ª atividade: "
            )
        )

        if dias >= 0:
            soma_dias += dias
            atividade += 1
        else:
            print("Quantidade de dias informada inválida.")
            continue

    print(
        f"O tempo total para concluir as atividades do projeto foi de {soma_dias} dias."
    )


def main():
    calculo_tempo_total_projeto()


if __name__ == "__main__":
    main()
