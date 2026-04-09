# Se o arquivo main estiver dentro da mesma pasta não é preciso puxar também o diretório da pasta.
from modelos_app_restaurante.restaurante import Restaurante
from modelos_app_restaurante.cardapio.bebida import Bebida
from modelos_app_restaurante.cardapio.prato import Prato


def main():
    # criando os restaurantes
    restaurante_mexicano = Restaurante(
        "escalantes texmex", "comida mexicana", "16h às 00h"
    )

    bebida_suco = Bebida("suco de melância", 8.50, "350ml")
    prato_nachos = Prato(
        "nachos", 29.90, "nachos com delicioso molho de queijo cremoso"
    )

    restaurante_mexicano.adicionar_ao_cardapio(bebida_suco)
    restaurante_mexicano.adicionar_ao_cardapio(prato_nachos)

    # implementando a avaliação para o restaurante
    restaurante_mexicano.receber_avaliacao("Guilherme", 5)
    restaurante_mexicano.receber_avaliacao("Gabriella", 5)
    restaurante_mexicano.receber_avaliacao("Maria", 10)

    # listando todos os restaurantes
    Restaurante.listar_restaurantes()
    print()

    restaurante_mexicano.exibir_cardapio


if __name__ == "__main__":
    main()
