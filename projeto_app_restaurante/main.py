# Se o arquivo main estiver dentro da mesma pasta não é preciso puxar também o diretório da pasta.
from modelos_app_restaurante.restaurante import Restaurante
from modelos_app_restaurante.cardapio.bebida import Bebida
from modelos_app_restaurante.cardapio.prato import Prato
from modelos_app_restaurante.cardapio.sobremesa import Sobremesa


def main():
    # Criando os restaurantes
    restaurante_mexicano = Restaurante(
        "escalantes texmex", "comida mexicana", "16h às 00h"
    )

    # Instanciando as bebidas do cardápio
    bebida_mexicano_suco = Bebida("suco de melância", 4.50, "350ml")
    bebida_mexicano_refri1 = Bebida("coca-cola", 6.90, "350 ml")
    bebida_mexicano_refri2 = Bebida("guaraná antartica", 5.90, "350 ml")
    # Instanciando os pratos do cardápio
    prato_mexicano_nachos = Prato(
        "nachos", 19.90, "nachos com delicioso molho de queijo cheddar cremoso."
    )
    prato_mexicano_tacos = Prato(
        "tacos",
        29.90,
        "deliciosos tacos com vinagrete, molhos da casa e recheio(carne moída, frango ou vegetariano)",
    )
    prato_mexicano_tortilhas = Prato(
        "tortilhas",
        38.50,
        "tortilhas tostadas e macias com guacamole, molhos da casa e recheio(carne moída, frango ou vegetariano)",
    )
    # Instanciando as sobremesas do cardápio
    sobremesa_mexicano_bolo = Sobremesa(
        "bolo três leches",
        15,
        "bolo esponjoso embebido em três tipos de leite, coberto com chantilly, frutas e canela",
    )
    sobremesa_mexicano_jericalla = Sobremesa(
        "jericalla",
        9.9,
        "semelhante a um crème brûlée, distingue-se pela sua superfície caramelizada/queimada",
    )
    sobremesa_mexicano_churros = Sobremesa(
        "churros",
        10.9,
        "5 saborosos mini churros salpicados com uma camada de açúcar por fora e recheado com doce de leite",
    )

    # Adicionando as instâncias criados ao cardápio específico
    restaurante_mexicano.adicionar_ao_cardapio(bebida_mexicano_suco)
    restaurante_mexicano.adicionar_ao_cardapio(bebida_mexicano_refri1)
    restaurante_mexicano.adicionar_ao_cardapio(bebida_mexicano_refri2)
    restaurante_mexicano.adicionar_ao_cardapio(prato_mexicano_nachos)
    restaurante_mexicano.adicionar_ao_cardapio(prato_mexicano_tacos)
    restaurante_mexicano.adicionar_ao_cardapio(prato_mexicano_tortilhas)
    restaurante_mexicano.adicionar_ao_cardapio(sobremesa_mexicano_bolo)
    restaurante_mexicano.adicionar_ao_cardapio(sobremesa_mexicano_jericalla)
    restaurante_mexicano.adicionar_ao_cardapio(sobremesa_mexicano_churros)

    # implementando a avaliação para o restaurante específico
    restaurante_mexicano.receber_avaliacao("Guilherme", 5)
    restaurante_mexicano.receber_avaliacao("Gabriella", 5)
    restaurante_mexicano.receber_avaliacao("Maria", 10)
    restaurante_mexicano.receber_avaliacao("Pedro", 3.5)

    # listando todos os restaurantes
    Restaurante.listar_restaurantes()
    print()

    # Aplicando os descontos para os produtos de um restaurante específico
    bebida_mexicano_suco.aplicar_desconto()
    prato_mexicano_nachos.aplicar_desconto()
    prato_mexicano_tacos.aplicar_desconto()
    sobremesa_mexicano_churros.aplicar_desconto()

    # Exibindo o cardápio atualizado com os descontos aplicados
    restaurante_mexicano.exibir_cardapio


if __name__ == "__main__":
    main()
