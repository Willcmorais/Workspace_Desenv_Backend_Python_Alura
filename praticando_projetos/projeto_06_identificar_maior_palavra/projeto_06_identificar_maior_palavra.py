# identificar a maior palavra no texto
# identificar as palavras com mais de 10 letras


def formatar_texto():
    texto = input("Informe aqui o seu texto: ")
    texto = texto.lower()
    caracteres_especiais = ",.!|?;:\"'()[]{}"

    for caractere in caracteres_especiais:
        texto = texto.replace(caractere, "")
    return texto


def identificar_maior_palavra():
    contador_palavras_longas = []
    texto_formatado = formatar_texto()

    for palavra in texto_formatado.split():
        if len(palavra) >= 10:
            contador_palavras_longas.append(palavra)

    if contador_palavras_longas:
        print("\nPalavras longas encontradas: \n")
        for palavra in contador_palavras_longas:
            print(palavra)
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")


def main():
    identificar_maior_palavra()
