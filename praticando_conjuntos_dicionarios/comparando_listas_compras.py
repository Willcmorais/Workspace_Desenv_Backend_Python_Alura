# Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

# Quais itens apareceram nas duas listas
# Quais foram exclusivos de Laura
# Quais foram exclusivos da Ana

# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

lista_compras_laura = set(
    input("\nInforme os itens da lista da Laura(separados por vírgula): ")
    .lower()
    .split(", ")
)

lista_compras_ana = set(
    input("\nInforme os itens da lista da Ana(separados por vígula): ")
    .lower()
    .split(", ")
)

itens_iguais = lista_compras_laura.intersection(lista_compras_ana)
itens_exclusivos_laura = lista_compras_laura.difference(lista_compras_ana)
itens_exclusivos_ana = lista_compras_ana.difference(lista_compras_laura)

print(f"Itens iguais nas listas: {', '.join(itens_iguais)}")
print(f"Itens exclusivos da lista de Laura: {', '.join(itens_exclusivos_laura)}")
print(f"Itens exclusivos da lista de Ana: {itens_exclusivos_ana}")
