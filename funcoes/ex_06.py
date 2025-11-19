import os

# Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário. Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().


def numeros_pares(numeros):
    return list(filter(lambda x: x % 2 == 0, numeros))


def main():
    valores = input("Informe os números separados por espaço: ").split()
    numeros = list(map(lambda x: int(x), valores))
    os.system("cls")
    print(f"Listagem informada: {numeros}")
    print(f"Listagem apenas dos números pares: {numeros_pares(numeros)}")


if __name__ == "__main__":
    main()
