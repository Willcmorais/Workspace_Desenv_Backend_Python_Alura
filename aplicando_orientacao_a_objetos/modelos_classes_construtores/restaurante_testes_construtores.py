class Restaurante:
    restaurantes = []

    # Quando definimos um método construtor queremos dizer que ao instanciar um objeto de uma classe ele já terá os atributos que definirmos. Porém, precisamos definir também os parâmetros no nosso método __init__. Dentro dele vamos colocar o self. É uma palavra chave que informa que cada instância criada através da classe vai conter apenas as informações daquele objeto e ao criar o objeto essas informações serão vinculadas apenas a ele. Por convencão utilizamos o self para referenciar, seria como um this também. Porém, qualquer nome poderia ser informado.
    def __init__(
        self,
        nome="",
        categoria="",
        ativo=False,
        horario_funcionamento="",
        area_de_delivery="",
    ):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.horario_funcionamento = horario_funcionamento
        self.area_de_delivery = area_de_delivery
        # Adiciona automaticamente a instância atual da classe Restaurante à lista restaurantes, que é um atributo de classe, porque é definida diretamente dentro do escopo da classe e fora de qualquer método específico.
        Restaurante.restaurantes.append(self)

    # def __str__(self):
    #     return f"Nome do restaurante: {self.nome} | Categoria: {self.categoria} | Status: {self.ativo}."

    def listar_restaurantes():
        print(
            "Listagem de restaurantes(Nome, Categoria, Ativo, Horário de Funcionamento e Área de Delivery)\n"
        )
        for restaurante in Restaurante.restaurantes:
            print(
                f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.horario_funcionamento} | {restaurante.area_de_delivery}"
            )


restaurante_japones = Restaurante(
    "Yakuzô Sushi & Lounge Bar",
    "Comida Japônesa",
    True,
    "18h às 00h",
    "Zonas Sul e Norte",
)

restaurante_italiano = Restaurante("Terraço do Marconi", "Comida Italiana")

Restaurante.listar_restaurantes()
