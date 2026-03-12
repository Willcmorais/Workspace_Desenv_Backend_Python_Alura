import random

# A senha teve conter letras miúsculas, minúsculas, números, caracteres especiais e ter no mínimo 12 caracteres.


def criar_senha_aleatoria():
    minusculas = "abcdefghijklmnopqrstuvxwyz"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    caracteres_especiais = "!@#$%&*"
    numeros = "0123456789"

    # garante que tenha pelo menos as 4 obrigações na senha.
    senha = [
        random.choice(minusculas),
        random.choice(maiusculas),
        random.choice(caracteres_especiais),
        random.choice(numeros),
    ]

    # Cria uma variável que une todas as outras variáveis
    todos_caracteres = minusculas + maiusculas + caracteres_especiais + numeros

    # Utiliza a função extend para adicionar todos os caracteres na senha já criada com os outros 4 caracteres.
    senha.extend(random.choices(todos_caracteres, k=8))

    # Reorganiza os caracteres da lista, evitando que os primeiros sejam sempre as 4 obrigações.
    random.shuffle(senha)

    # Reverte a lista para uma string
    return "".join(senha)
