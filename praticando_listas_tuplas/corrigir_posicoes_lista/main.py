# O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto. Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?


def main():
    lista_corredores = ["William", "Maria", "João", "Brbvuno", "Pedro", "Xavier"]
    print(f"Lista original:\n{lista_corredores}\n")

    nome_incorreto = input("Informe o nome incorreto: ").capitalize()

    if nome_incorreto in lista_corredores:
        nome_correto = input("Informe o nome atualizado: ").capitalize()
        posicao_nome_incorreto = lista_corredores.index(nome_incorreto)
        lista_corredores.remove(nome_incorreto)
        lista_corredores.insert(posicao_nome_incorreto, nome_correto)
        print(f"\nO nome {nome_incorreto} foi substituído por {nome_correto}.")
        print(f"\nLista atualizada:\n{lista_corredores}")
    else:
        print("Nome não encontrado.")


if __name__ == "__main__":
    main()
