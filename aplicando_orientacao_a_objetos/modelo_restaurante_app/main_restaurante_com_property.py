# Se o arquivo main estiver dentro da mesma pasta não é preciso puxar também o diretório da pasta.
from restaurante_com_property import Restaurante

restaurante_mexicano1 = Restaurante(
    "escalantes texmex", "comida mexicana", "16h às 00h"
)
restaurante_japones1 = Restaurante("mianzô", "comida japonesa", "18h às 23h")
restaurante_brasileiro1 = Restaurante(
    "comedoria da cona ana", "comida caseira", "11h às 19h"
)

# alternando o status do restaurante para ativo
restaurante_mexicano1.alternar_status()


def main():
    # listando todos os restaurantes
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
