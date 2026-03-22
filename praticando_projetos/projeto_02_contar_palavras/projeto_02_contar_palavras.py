import os


def mostrar_menu():
    print("*" * 30)
    print("==== CONTADOR DE PALAVRAS ====")
    print("*" * 30)


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def limpar_texto(texto):
    """
    A função vai formatar o texto informado pelo usuário;
    Transforma tudo em minúsculo e retira os caracteres especiais;
    Feito isso ele vai retornar a frase limpa.
    """
    texto = texto.lower()
    caracteres_especiais = ",.!|?;:\"'()[]{}"

    for caractere in caracteres_especiais:
        texto = texto.replace(caractere, "")

    return texto


def contar_palavras(frase):
    """
    A função faz a contagem de palavras de uma frase informada pelo usuário;
    Caso nada seja informado ele vai criar um dicionário vazio;
    Caso tenha algo vai separar a frase com o split para iterar;
    Será criado um dicionário para controle de palavras;
    Faz uma iteração com as palavras da lista;
    Caso na iteração a palavra já exista ela não vai ser adicionada;
    Caso não existe ela vai ser adicionada ao dicionário para controle;
    Feito isso será retornado o dicionário da contagem.
    """
    frase = limpar_texto(frase)

    if not frase.strip():
        return {}

    palavras = frase.split()
    contagem = {}

    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem


def receber_texto():
    while True:
        frase = input("Informe a sua frase: ").strip()

        if not frase:
            print("Erro: Nada foi digitado.")
            limpar_tela()
            continue
        else:
            contagem_de_palavras = contar_palavras(frase)
            if contagem_de_palavras:
                for palavra, quantidade in contagem_de_palavras.items():
                    print(f"{palavra} : {quantidade}")
        break


def main():
    mostrar_menu()
    receber_texto()
