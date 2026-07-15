def formatar_texto(texto):
    texto = texto.lower().strip()
    return texto


def contar_vogais_texto():
    vogais = "aeiouàáèéìíòóùúâêîôûãõ"
    contagem_de_vogais = {}

    texto = input("Informe aqui um texto: ")

    texto_formatado = formatar_texto(texto)

    for letra in texto_formatado:
        if letra in vogais:
            contagem_de_vogais[letra] = contagem_de_vogais.get(letra, 0) + 1
    return contagem_de_vogais


def mostrar_resultado(contagem_de_vogais):
    print(f"\nO texto contém {len(contagem_de_vogais)} vogais.\n")
    print("Listagem das vogais contidas no texto:\n")

    for letra, quantidade in contagem_de_vogais.items():
        print(f"Vogal: {letra} -> Quantidade: {quantidade}.")


def main():
    contagem_de_vogais = contar_vogais_texto()
    mostrar_resultado(contagem_de_vogais)
