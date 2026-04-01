# Se o arquivo main estiver dentro da mesma pasta não é preciso puxar também o diretório da pasta.
from modelos_app_restaurante.restaurante import Restaurante


def main():
    # criando os restaurantes
    restaurante_mexicano = Restaurante(
        "escalantes texmex", "comida mexicana", "16h às 00h"
    )

    # implementando a avaliação para o restaurante
    restaurante_mexicano.receber_avaliacao("Guilherme", 5)
    restaurante_mexicano.receber_avaliacao("Gabriella", 5)
    restaurante_mexicano.receber_avaliacao("Maria", 10)

    # listando todos os restaurantes
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
