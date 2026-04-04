from modulos.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    # Implemento do Método Especial __str__ na Classe Filha: Adiciona um método especial __str__ à classe Carro que estenda o método da classe pai (Veiculo).
    def __str__(self):
        return f"{super().__str__()} | Portas: {self._portas}"
