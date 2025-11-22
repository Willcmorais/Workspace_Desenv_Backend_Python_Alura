# Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário. Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.


def somar_numeros(numero):
    if numero == 1:
        return 1
    return numero + somar_numeros(numero - 1)


def main():
    numero = int(input("Informe um número inteiro: "))
    print(somar_numeros(numero))


if __name__ == "__main__":
    main()
