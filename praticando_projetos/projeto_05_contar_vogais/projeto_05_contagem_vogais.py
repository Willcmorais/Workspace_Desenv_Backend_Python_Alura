# contar quantas vogais há em um texto


def formatar_texto(texto):
    texto = texto.lower().strip()
    return texto


def contar_vogais(texto):
    formatar_texto(texto)
    vogais = "aeiouàáèéìíòóùúâêîôûãõ"
    contador_de_vogais = {}

    for letra in texto:
        if letra in vogais:
            contador_de_vogais[letra] = contador_de_vogais.get(letra, 0) + 1
    return contador_de_vogais
