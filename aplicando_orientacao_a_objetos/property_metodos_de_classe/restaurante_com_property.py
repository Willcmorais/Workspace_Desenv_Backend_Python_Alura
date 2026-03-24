class Restaurante:
    lista_de_restaurantes = []

    def __init__(self, nome="", categoria="", horario_funcionamento=""):
        self.nome = nome
        self.categoria = categoria
        self.nota = "0"
        self.horario_funcionamento = horario_funcionamento
        self._status = False
        Restaurante.lista_de_restaurantes.append(self)

    def listar_restaurantes():
        print("-" * 48, "LISTA DE RESTAURANTES", "-" * 48, "\n")
        # Como estamos fazendo operações com os nomes, colocamos eles entre { }. Caso contrário não conseguiríamos justificar igual ao print do loop
        print(
            f"{"Nome do restaurante:".ljust(25)} | {"Categoria:".ljust(25)} | {"Nota:".ljust(25)} | {"Horário:".ljust(25)} | Status:"
        )
        for restaurante in Restaurante.lista_de_restaurantes:
            print(
                f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.nota.ljust(25)} | {restaurante.horario_funcionamento.ljust(25)} | {restaurante.status}"
            )
        print("-" * 119)

    # O property é usado para encapsular o atributo da classe, e criar a partir dele um método. Esse método vai fazer uma certa ação de acordo com a lógica criada
    @property
    def status(self):
        return "✅" if self._status else "❎"


restaurante_mexicano1 = Restaurante(
    "Escalantes TexMex", "Comida Mexicana", "16h às 00h"
)
restaurante_japones1 = Restaurante("Mianzô", "Comida Japonesa", "18h às 23h")
restaurante_brasileiro1 = Restaurante(
    "Comedoria da Dona Ana", "Comida Caseira", "11h às 19h"
)

Restaurante.listar_restaurantes()
