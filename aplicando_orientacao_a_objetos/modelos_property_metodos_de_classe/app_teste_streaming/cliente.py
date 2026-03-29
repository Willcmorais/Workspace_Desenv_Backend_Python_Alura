class Cliente:
    def __init__(self, nome, email, plano):
        self._nome = nome.title()
        self._email = email
        self._planos = ["Basic", "Medium", "Premium"]
        self._plano = plano.title()

        if self._plano in self._planos:
            self._plano
        else:
            print(f"Plano '{plano}' inválido.")

    def __str__(self):
        return f"{self._nome} | {self._email} | {self._plano}."

    def mudar_plano(self, nome_cliente, plano):
        if plano.title() in self._planos:
            if plano == "Basic":
                print("Plano ")
        else:
            print("O plano escolhido não está disponível.")
