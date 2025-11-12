# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado

# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.


def calculo_de_medias():
    """
    Esta função vai calcular a média dos alunos, pegando 3 notas e dividindo pela quantidade de notas.

    Inputs:
    - Notas

    Outputs:
    - Soma;
    - Média;
    - Resultado do aluno referente à média(aprovado, reprovado, recuperação).
    """

    soma = 0
    media = 0

    for nota in range(1, 4):
        notas = float(input(f"Informe a {nota}ª nota: "))
        soma += notas

    media = soma / 3

    if media >= 7:
        print(f"A média do aluno foi {media:.1f}. Foi aprovado.")
    elif 5 <= media < 7:
        print(f"A média do aluno foi {media:.1f}. Está na recuperação.")
    else:
        print(f"A média do aluno foi {media:.1f}. Está reprovado.")


def main():
    calculo_de_medias()


if __name__ == "__main__":
    main()
