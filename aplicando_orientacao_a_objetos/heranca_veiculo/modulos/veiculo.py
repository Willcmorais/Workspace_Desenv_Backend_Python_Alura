from abc import abstractmethod


class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca.title()
        self._modelo = modelo.title()
        self._ligado = False

    def __str__(self):
        return f"Marca: {self._marca} | Modelo: {self._modelo} | Estado: {self.ligado}"

    @property
    def ligado(self):
        return "Ligado" if self._ligado else "Desligado"

    @abstractmethod
    def ligar(self):
        pass
