# André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.

# Qual é o problema do código de André e como resolver?

contador = 0

while contador < 10:
    print("Processando dados...")

    # Resolução do problema.
    contador += 1
