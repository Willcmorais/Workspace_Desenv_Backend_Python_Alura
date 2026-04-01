# Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.

# Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?


class GerenciadorLista:
    def __init__(self):
        self._convidados = []

    def adicionar_convidados(self, convidados):
        for convidado in convidados:
            self._convidados.append(convidado.strip())

    def remanejar_novo_convidado(self, posicao, convidado):
        self._convidados.insert(posicao, convidado)

    def mostrar_lista(self):
        print("--- Lista de convidados ---")
        for convidado in self._convidados:
            print(f"- {convidado}")
