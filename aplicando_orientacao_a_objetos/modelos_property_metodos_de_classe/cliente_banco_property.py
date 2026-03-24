class ClienteBanco:
    ano_atual = 2026

    def __init__(
        self, _nome="", _ano_nasc=0, _profissao="", _estado_civil="", _nacionalidade=""
    ):
        self._nome = _nome.title()
        self._ano_nasc = _ano_nasc
        self._profissao = _profissao.title()
        self._estado_civil = _estado_civil.title()
        self._nacionalidade = _nacionalidade.capitalize()
        self._status = False

    def __str__(self):
        return f"Cliente: {self._nome}\nIdade: {self.idade}\nProfissão: {self._profissao}\nEstado Civil: {self._estado_civil}\nEndereço: {self._nacionalidade}\nStatus: {self.status}"

    @property
    def idade(self):
        return self.ano_atual - self._ano_nasc

    @property
    def status(self):
        return "Ativo" if self._status else "Inativo"

    def alternar_status(self):
        self._status = not self._status
        return print(f"Status do cliente {self._nome} alterado com sucesso!\n")


cliente1 = ClienteBanco(
    "william morais", 1996, "desenvolvedor backend", "solteiro", "brasileiro"
)
cliente2 = ClienteBanco(
    "carlos magno", 1976, "desenvolvedor frontend", "viúvo", "italiano"
)
cliente3 = ClienteBanco("joão carlos", 1990, "pedreiro", "casado", "brasileiro")

print(cliente1)
print("-" * 20)
cliente1.alternar_status()
print(cliente1)
print("-" * 20)
print(cliente2)
print("-" * 20)
print(cliente3)
