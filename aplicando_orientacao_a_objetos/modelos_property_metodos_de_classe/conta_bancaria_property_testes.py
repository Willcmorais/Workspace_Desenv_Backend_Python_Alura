class ContaBancaria:
    def __init__(self, titular="", saldo=0.0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Nome do titular: {self._titular} | Saldo: R${self._saldo} | Status: {self._ativo}"

    # métodos de atributos read-only
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def ativar_conta(self):
        self._ativo = not self._ativo
        return print("Conta ativada com sucesso!")


conta1 = ContaBancaria("Marcos Vinícius", 2500.98)
conta2 = ContaBancaria("José Vincente", 980.99)

print(conta1)
conta1.ativar_conta()
print(conta1.saldo)
# conta1.saldo = 9000 ; Isso não pode ser feito, pois estamos protegente o nosso atributo da classe do mundo externo
print()


print(conta2)
conta2.ativar_conta()
print(conta2)
