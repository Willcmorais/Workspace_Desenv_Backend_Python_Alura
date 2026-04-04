from modelos_app_restaurante.cardapio.item_cardapio import ItemCardapio


# Para indicar que essa classe é um "filho(a)" da classe mãe colocaremos a classe mãe sendo referenciada dentro de parênteses. Isso quer dizer que a classe Prato vai poder utilizar todas as classes e atributos da classe mãe.class Bebida(ItemCardapio):
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        # O método super permite que acessemos as informações da outra classe. Vai fazer com que ao instânciar um objeto do tipo prato ele já instância também o init da classe mãe ItemCardapio com nome e preco.
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
