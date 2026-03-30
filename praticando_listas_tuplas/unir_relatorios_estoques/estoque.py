# Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?


class Estoque:
    def __init__(self, proprietario_estoque):
        self._proprietario_estoque = proprietario_estoque
        self._estoque1 = (
            "Arroz",
            "Feijão",
            "Macarrão",
            "Carne",
            "Frango",
        )
        self._estoque2 = (
            "Peixe",
            "Cenoura",
            "Alface",
            "Suco",
            "Iogurte",
        )

    def __str__(self):
        return f"Estoque 1: {self._estoque1}\nEstoque 2: {self._estoque2}"

    def unificar_estoque(self):
        self._estoque_unificado = self._estoque1 + self._estoque2
        return self._estoque_unificado

    def listar_estoque(self):
        print("--- Lista do estoque unificado ---")
        for produto in self._estoque_unificado:
            print(f"- {produto}")
