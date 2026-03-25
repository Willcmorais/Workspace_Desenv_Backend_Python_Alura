# Se o arquivo main estiver dentro da mesma pasta não é preciso puxar também o diretório da pasta.
from restaurante_com_property import Restaurante

restaurante_mexicano = Restaurante("escalantes texmex", "comida mexicana", "16h às 00h")
restaurante_mexicano.receber_avaliacao("Guilherme", 10)
restaurante_mexicano.receber_avaliacao("Gabriella", 8)
restaurante_mexicano.receber_avaliacao("Maria", 5)


def main():
    # listando todos os restaurantes
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
