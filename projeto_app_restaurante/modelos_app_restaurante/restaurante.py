from avaliacao_restaurante import Avaliacao


class Restaurante:
    """Representa um restaurante e suas características."""

    lista_de_restaurantes = []

    def __init__(self, nome="", categoria="", horario_funcionamento=""):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        - horario_funcionamento (str): O horário de funcionamento do restaurante.
        """

        # atributos protegidos
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._horario_funcionamento = horario_funcionamento
        self._status = False
        self._avaliacao = []
        Restaurante.lista_de_restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f"{self._nome} | {self._categoria} | {self._horario_funcionamento} | {self._status}"

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print("-" * 48, "LISTA DE RESTAURANTES", "-" * 48, "\n")
        # Como estamos fazendo operações com os nomes, colocamos eles entre { }. Caso contrário não conseguiríamos justificar igual ao print do loop
        print(
            f"{"Nome do restaurante:".ljust(25)} | {"Categoria:".ljust(25)} | {"Horário:".ljust(25)} | {"Avaliação:".ljust(25)} | Status:"
        )
        for restaurante in cls.lista_de_restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._horario_funcionamento.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.status}"
            )
        print("-" * 119)

    # O property é usado para encapsular o atributo da classe, e criar a partir dele um método. Esse método vai fazer uma certa ação de acordo com a lógica criada, modificando a visualização padrão
    @property
    def status(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return "✅" if self._status else "❎"

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        # se não tivermos nenhuma avaliação vai retornar zero
        if not self._avaliacao:
            return "-"
        # pegue todas as avaliações e para cada avaliação só queremos a nota, vamos somar a nota
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media_das_notas = round(soma_das_notas / quantidade_de_notas, 1)
        return media_das_notas

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    # alterna o status, se for True fica False e vice-versa
    def alternar_status(self):
        """Alterna o estado de atividade do restaurante."""
        self._status = not self._status
