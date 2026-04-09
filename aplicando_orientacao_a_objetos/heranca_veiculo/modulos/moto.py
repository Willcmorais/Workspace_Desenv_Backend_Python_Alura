from modulos.veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo.title()

    def __str__(self):
        return f"{super().__str__()} | Tipo: {self._tipo}"

    def ligar(self):
        self._ligado = True
        print(f'A moto {self._modelo} foi ligada.')