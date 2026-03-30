# Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.

# Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?


class GerenciadorLista:
    def __init__(self):
        self._lista_convidados = ["Mario", "Carlos", "Jorge", "Maria"]

    def __str__(self):
        return f"Lista de convidados:\n {self._lista_convidados}"

    def adicionar_convidado(self, posicao: int, convidado: str):
        self._lista_convidados.insert(posicao, convidado)

    def mostrar_lista(self):
        for convidado in self._lista_convidados:
            print(f"- {convidado}")
