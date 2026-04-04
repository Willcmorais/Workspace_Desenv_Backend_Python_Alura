from modulos.banco import Banco


class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self):
        return f"Agência: {self._nome} | Endereço: {self._endereco} | Nº {self._numero}"
