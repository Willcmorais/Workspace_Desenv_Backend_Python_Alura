from projeto_05_contagem_vogais import contar_vogais

# pedir um texto qualquer

texto = input("Informe aqui o seu texto: ")

print(f"O texto contém {len(contar_vogais(texto))} vogais.")
print(f"Listagem das vogais: {contar_vogais(texto)}")
