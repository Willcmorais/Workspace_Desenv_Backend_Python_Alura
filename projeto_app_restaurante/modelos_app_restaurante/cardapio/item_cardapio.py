# Aqui vamos intruduzir o conceito de Herança. A ideia é, queremos que qualquer tipo de item do cardápio, seja bebida ou comida, herdem os mesmos atributos da "Classe Mãe - ItemCardapio". Pois, podemos ver que tanto pratos como bebidas tem os mesmos atributos que podem ser introduzidos em apenas uma classe e herdada por eles depois.


class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome.title()
        self._preco = preco
