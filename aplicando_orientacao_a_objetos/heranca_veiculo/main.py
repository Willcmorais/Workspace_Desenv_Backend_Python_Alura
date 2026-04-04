from modulos.carro import Carro
from modulos.moto import Moto


def main():
    carro1 = Carro("volkswagen", "polo", 4)
    carro2 = Carro("range rover", "evoque", 4)
    carro3 = Carro("lamborghini", "temerario", 2)

    moto1 = Moto("harley davidson", "fat boy", "cruiser")
    moto2 = Moto("kawasaki", "ninja 300", "sport")
    moto3 = Moto("honda", "tornado", "racing")

    print(carro1)
    print(carro2)
    print(carro3)
    print()
    print(moto1)
    print(moto2)
    print(moto3)


if __name__ == "__main__":
    main()
