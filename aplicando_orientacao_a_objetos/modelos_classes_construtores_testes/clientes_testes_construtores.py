class Cliente:
    clientes = []

    def __init__(
        self, nome="", idade=0, profissao="", telefone="", email="", status=False
    ):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.telefone = telefone
        self.email = email
        self.status = status
        Cliente.clientes.append(self)

    def listar_clientes():
        print(
            "Listagem de clientes(Nome, Idade, Profissão, Telefone, Email e Status(ativo))\n"
        )

        for cliente in Cliente.clientes:
            print(
                f"{cliente.nome} | {cliente.idade} | {cliente.profissao} | {cliente.telefone} | {cliente.email} | {cliente.status}"
            )


cliente1 = Cliente(
    "William Coelho de Morais",
    29,
    "Desenvolvedor Backend",
    "(87) 98558-9856",
    "desenvolvedor@gmail.com",
    True,
)
cliente2 = Cliente(
    "Victoria Maria Ferreira dos Anjos",
    27,
    "Ginecologista e Obstetra",
    "(99) 998745-3335",
    "",
    True,
)
cliente3 = Cliente(
    "Manoel José Paula de Morais", 61, "Advogado", "", "advogado@gmail.com"
)

Cliente.listar_clientes()
