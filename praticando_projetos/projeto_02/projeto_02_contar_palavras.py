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
