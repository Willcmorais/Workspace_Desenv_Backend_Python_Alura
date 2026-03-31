# Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?


class Estoque:
    _estoque_geral = []

    def __init__(self, proprietario):
        self._proprietario = proprietario
        self._estoque = ()

    def adicionar_ao_estoque(self):
        print(f"--- {self._proprietario} ---")
        entrada = input(
            "Informe o que quer adicionar ao estoque separado por vírgula: "
        ).split(",")

        entrada_refatorada = tuple(item.title().strip() for item in entrada)

        self._estoque += entrada_refatorada

        self._estoque_geral += self._estoque

    def listar_estoque(self):
        print(f"--- Lista {self._proprietario} ---")
        for produto in self._estoque:
            print(f"- {produto}")

    def listar_estoque_geral(self):
        print(f"--- {self._proprietario} ---")
        for produto in self._estoque_geral:
            print(f"- {produto}")
