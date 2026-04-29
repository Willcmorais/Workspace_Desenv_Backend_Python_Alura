# Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

texto1 = set(input("Informe o texto 1: ").lower().split())
texto2 = set(input("Informe o texto 2: ").lower().split())

palavras_comuns = texto1.intersection(texto2)

print(f"Palavras em comum nos textos: {palavras_comuns}")

# texto1 = input("\nInforme o primeiro texto: ")
# texto2 = input("\nInforme o segundo texto: ")

# palavras_texto1 = texto1.split()
# palavras_texto2 = texto2.split()
# palavras_iguais = set()

# for palavra1 in palavras_texto1:
#     for palavra2 in palavras_texto2:
#         if palavra1 == palavra2:
#             palavras_iguais.add(palavra1)

# print(f"Palavras em comum: {palavras_iguais}")
