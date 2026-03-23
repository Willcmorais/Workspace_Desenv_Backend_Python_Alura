class Carro:
    carros = []

    def __init__(self, nome="", marca="", cor="", ano=0):
        self.nome = nome
        self.marca = marca
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def listar_carros():
        print("Listagem de carros catalogados(Nome, Marca, Cor e Ano)\n")
        for carro in Carro.carros:
            print(f"{carro.nome} | {carro.marca} | {carro.cor} | {carro.ano}")


carro1 = Carro("Chevette", "Chevrolet", "Azul", 1973)
carro2 = Carro("Gol", "Volkswagen", "Cinza Escuro")
carro3 = Carro("Dolphin", "BYD", "Preto", 2026)

Carro.listar_carros()
