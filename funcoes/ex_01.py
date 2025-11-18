# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.


def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento


def main():
    nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))

    idade = calcular_idade(nascimento, ano_atual)

    print(f"Sua idade atual é {idade} anos.")


if __name__ == "__main__":
    main()
