# Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?


class Estoque:
    def __init__(self, proprietario):
        self._proprietario = proprietario
        self._estoque = ()

    def solicitar_entrada(self):
        print(f"--- {self._proprietario} ---")

        entrada = input(
            "Adicione aqui ao seu estoque (digite os itens separados por vírgula): "
        ).split(",")

        entrada_refatorada = tuple(item.title().strip() for item in entrada)

        return entrada_refatorada

    def adicionar_ao_estoque(self, produtos):
        self._estoque += produtos

    def listar_estoque(self):
        print(f"--- Lista {self._proprietario} ---")
        for produto in self._estoque:
            print(f"- {produto}")

    def unificar_estoques(self, *estoques):
        print("--- Relatório Estoque Geral ---")
        estoque_total = self._estoque

        for estoque in estoques:
            estoque_total += estoque._estoque

        for produto in estoque_total:
            print(f"- {produto}")
