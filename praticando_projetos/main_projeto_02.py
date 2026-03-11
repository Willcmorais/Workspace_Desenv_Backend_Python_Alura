from projeto_02_contar_palavras import contar_palavras

frase = input("Informe a sua frase: ").strip()

if not frase:
    print("Erro: Nada foi digitado.")
else:
    resultado = contar_palavras(frase)
    if resultado:
        for palavra, quantidade in resultado.items():
            print(f"{palavra} : {quantidade}")
    else:
        print(f"Nenhuma palavra válida foi encontrada.")
