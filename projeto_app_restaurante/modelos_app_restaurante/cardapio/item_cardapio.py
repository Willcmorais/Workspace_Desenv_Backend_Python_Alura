# Aqui vamos intruduzir o conceito de Herança. A ideia é, queremos que qualquer tipo de item do cardápio, seja bebida ou comida, herdem os mesmos atributos da "Classe Mãe - ItemCardapio". Pois, podemos ver que tanto pratos como bebidas tem os mesmos atributos que podem ser introduzidos em apenas uma classe e herdada por eles depois.

# Introduzindo ao conceito de métodos abstratos e polimorfismo. Vamos importar da biblioteca abstract base classes o modelo ABC com a função abstractmethod.
from abc import ABC, abstractmethod


# A classe ItemCardapio vai herdar o modelo ABC.
class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome.title()
        self._preco = preco

    # Esse método abstrato não precisa ser implementado no arquivo de ItemCardapio só precisamos informar que ele existe. Como ele é uma classe pai de bebidas, pratos, etc, esse método será agora obrigatório de existir nas classes filhas e poderá ser herdado e implementado a partir dessas classes.
    @abstractmethod
    def aplicar_desconto(self):
        pass
