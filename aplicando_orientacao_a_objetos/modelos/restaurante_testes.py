# ===== Classe criada com os atributos padrões =====
class Restaurante:

    nome = ""
    categoria = ""
    ativo = False


# ===== Instanciando um objeto da classe restaurante =====
restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet", "Italiana"


def mostrar_restaurante_praca():
    if restaurante_praca.ativo:
        print(f"O restaurante {restaurante_praca.nome} está ativo.")
    else:
        print(f"O restaurante {restaurante_praca.nome} está inativo.")

    print(
        f"Nome do Restaurante: {restaurante_praca.nome} - Categoria: {restaurante_praca.categoria} - Status: {restaurante_praca.ativo}"
    )


mostrar_restaurante_praca()
print()

# ===== Instanciando um outro objeto da classe restaurante =====

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "iFood"
restaurante_pizza.ativo = True


def mostrar_restaurante_pizza():
    if restaurante_pizza.ativo:
        print(f"O restaurante {restaurante_pizza.nome} está ativo.")
    else:
        print(f"O restaurante {restaurante_pizza.nome} está inativo.")

    if restaurante_pizza.categoria == "iFood":
        print("A categoria é iFood")
    else:
        print("A categoria não é iFood")
    print(
        f"Nome do Restaurante: {restaurante_pizza.nome} - Categoria: {restaurante_pizza.categoria} - Status: {restaurante_pizza.ativo}"
    )


mostrar_restaurante_pizza()

print()
restaurantes = [restaurante_praca, restaurante_pizza]
print(restaurantes)

# ===== Funções interessantes para se utilizar e entender melhor as classes =====

# Função dir lista todos os atributos, métodos e propriedades de um objeto.
print(
    f"\nFunção dir mostrando atributos, métodos e propriedades do objeto: {dir(restaurante_praca)}"
)

# Já a função vars vai mostrar um dicionário com todos os atributos e métodos do objeto.
print(
    f"\nFunção vars mostrando o dicionário com todos os atributos e métodos do objeto: {vars(restaurante_praca)}"
)
