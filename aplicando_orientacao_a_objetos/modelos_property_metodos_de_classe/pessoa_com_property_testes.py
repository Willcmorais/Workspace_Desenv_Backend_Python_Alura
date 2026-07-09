class Pessoa:
    def __init__(self, nome="", idade=0, profissao=""):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()

    def __str__(self):
        return f"{self._nome} | {self._idade} anos | {self._profissao}."

    # Isso DEVE ser um método normal, porque altera um dado (ação)
    def aniversario(self):
        self._idade += 1
        return f"Parabéns pelo seu aniversário {self._nome}! Você agora tem {self._idade} anos!"

    # Isso PODE ser uma property, porque apenas lê e formata dados
    @property
    def saudacao(self):
        if self._profissao:
            return f"Olá {self._nome}. Você é um(a) {self._profissao}(a) incrível!"
        else:
            return f"Olá {self._nome}. Falta você informar a sua profissão."


pessoa1 = Pessoa("william", 29, "programador")
pessoa2 = Pessoa("José", 33)
pessoa3 = Pessoa("Victoria", 27, "médico")

# Usando o métodos __str__ para printar as informações de usuário
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Usando a variável com property para mostrar atributos visuais e economizar memória com uma função a mais
print(pessoa1.aniversario)
print(pessoa2.aniversario)
print(pessoa3.aniversario)
print()

# Usando a variável com property para mostrar atributos visuais e economizar memória com uma função a mais
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
