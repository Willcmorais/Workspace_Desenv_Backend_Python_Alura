# Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.


class Despensa:
    def __init__(self, nome: str):
        self._nome = nome.title()
        self._produtos_despensa = set()

    def adicionar_produto_despensa(self):
        print(f"--- {self._nome} ---")
        entrada = input(
            "Informe os produtos que quer registrar separados por vírgula: "
        ).split(",")

        for produto in entrada:
            produto_refatorado = produto.strip().title()
            if not produto:
                continue
            if produto in self._produtos_despensa:
                print(f"⚠️ {produto_refatorado} já consta na {self._nome}.")
            else:
                print(
                    f"➕ {produto_refatorado} adicionado com sucesso na {self._nome}."
                )
                self._produtos_despensa.add(produto_refatorado)

    def verificar_produto(self):
        produto = input(f"{self._nome}\nInforme o nome produto que deseja verificar: ")
        produto_title = produto.title().strip()

        if produto_title not in self._produtos_despensa:
            print(f"❌ {produto_title} NÃO consta na {self._nome}. Precisa repor.")
        else:
            print(f"✅ {produto_title} já consta na {self._nome}.")

    def mostrar_despensa(self):
        print(f"--- {self._nome} ---\n")
        for indice, produto in enumerate(sorted(self._produtos_despensa), 1):
            print(f"{indice}.{produto}")
