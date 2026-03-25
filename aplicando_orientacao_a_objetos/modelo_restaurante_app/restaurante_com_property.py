from avaliacao_restaurante import Avaliacao


class Restaurante:
    lista_de_restaurantes = []

    def __init__(self, nome="", categoria="", horario_funcionamento=""):
        # atributos protegidos
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._horario_funcionamento = horario_funcionamento
        self._status = False
        self._avaliacao = []
        Restaurante.lista_de_restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria} | {self._horario_funcionamento} | {self._status}"

    @classmethod
    def listar_restaurantes(cls):
        print("-" * 48, "LISTA DE RESTAURANTES", "-" * 48, "\n")
        # Como estamos fazendo operações com os nomes, colocamos eles entre { }. Caso contrário não conseguiríamos justificar igual ao print do loop
        print(
            f"{"Nome do restaurante:".ljust(25)} | {"Categoria:".ljust(25)} | {"Horário:".ljust(25)} | Status:"
        )
        for restaurante in cls.lista_de_restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._horario_funcionamento.ljust(25)} | {restaurante.status}"
            )
        print("-" * 119)

    # O property é usado para encapsular o atributo da classe, e criar a partir dele um método. Esse método vai fazer uma certa ação de acordo com a lógica criada, modificando a visualização padrão
    @property
    def status(self):
        return "✅" if self._status else "❎"

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    # alterna o status, se for True fica False e vice-versa
    def alternar_status(self):
        self._status = not self._status
