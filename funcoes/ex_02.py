# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres. Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.


def contar_caracteres(palavra):
    contagem = len(palavra)
    return contagem


def main():
    palavra = input("Digite uma palavra: ")

    print(f"A palavra {palavra} tem {contar_caracteres(palavra)} caracteres.")


if __name__ == "__main__":
    main()
