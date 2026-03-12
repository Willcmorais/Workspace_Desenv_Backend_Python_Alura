# identificar a maior palavra no texto
# identificar as palavras com mais de 10 letras


def formatar_texto(texto):
    texto = texto.lower()
    caracteres_especiais = ",.!|?;:\"'()[]{}"

    for caractere in caracteres_especiais:
        texto = texto.replace(caractere, "")
    return texto


def identificar_maior_palavra(texto):
    formatar_texto(texto)
    contador_palavras_longas = []

    for palavra in texto.split():
        if len(palavra) >= 10:
            contador_palavras_longas.append(palavra)

    if contador_palavras_longas:
        print("Palavras longas encontradas: ")
        for palavra in contador_palavras_longas:
            print(palavra)
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")
