# Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.


class Despensa:
    def __init__(self, nome: str):
        self._nome = nome.title()
        self._produtos = {
            "Arroz",
            "Mostarda",
            "Feijão",
            "Macarrão",
            "Leite",
            "Batata",
            "Mandioca",
            "Carne Moída",
            "Coentro",
            "Peito de Frango",
            "Peixe",
        }

    def mostrar_despensa(self):
        print(f"--- {self._nome} ---\n")
        for indice, produto in enumerate(sorted(self._produtos), 1):
            print(f"{indice}. {produto}")

    def verificar_produto(self, produto: str):
        produto_title = produto.title()
        if not produto_title in self._produtos:
            print(f"❌ {produto_title} NÃO consta na {self._nome}. Precisa repor.")
        else:
            print(f"✅ {produto_title} já consta na {self._nome}.")

    def adicionar_produto_despensa(self, produto: str):
        produto_title = produto.title()
        if produto_title in self._produtos:
            print(f"⚠️ {produto_title} já consta na lista da {self._nome}.")
        else:
            self._produtos.add(produto_title)
            print(f"➕ {produto_title} adicionado com sucesso na {self._nome}.")
