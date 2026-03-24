class ClienteBanco:
    # Não usamos o _ nos argumentos do métodos
    def __init__(
        self, nome="", ano_nasc=0, profissao="", cpf="", nacionalidade="Brasileiro"
    ):
        self._nome = nome.title()
        self._ano_nasc = ano_nasc
        self._profissao = profissao.title()
        self._cpf = cpf
        self._nacionalidade = nacionalidade.capitalize()
        self._ano_atual = 2026
        self._status = False

    def __str__(self):
        return f"Cliente: {self._nome}\nIdade: {self.idade}\nProfissão: {self._profissao}\nCPF: {self._cpf}\nEndereço: {self._nacionalidade}\nStatus: {self.status}"

    @property
    def idade(self):
        return self._ano_atual - self._ano_nasc

    @property
    def status(self):
        return "Ativo" if self._status else "Inativo"

    def alternar_status(self):
        self._status = not self._status
        # Retornamos o novo valor caso queira usar em uma validação depois
        return self._status

    # redundância, pois o método construtor já faz esse serviço
    # @classmethod
    # def criar_conta(cls, nome, ano_nasc, profissao, cpf, nacionalidade):
    #     conta = ClienteBanco(nome, ano_nasc, profissao, cpf, nacionalidade)
    #     return conta


cliente1 = ClienteBanco(
    "william", 1996, "desenvolvedor backend", 14589555502, "brasileiro"
)
cliente2 = ClienteBanco(
    "lindsey", 1987, "desenvolvedora frontend", 12532578525, "americana"
)
cliente3 = ClienteBanco("mario", 1980, "design de interiores", 12225874585, "português")
cliente4 = ClienteBanco("jorge", 1989, "advogado criminal", 12225874585)

print(cliente1)
print("-" * 20)
cliente1.alternar_status()
print(cliente1)
print("-" * 20)
print(cliente2)
print("-" * 20)
print(cliente3)
print("-" * 20)
print(cliente4)
