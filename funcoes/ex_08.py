# Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números. Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.


def calcular():
    somar = lambda v1, v2: (primeiro_numero + segundo_numero)
    subtrair = lambda v1, v2: (primeiro_numero - segundo_numero)
    multiplicar = lambda v1, v2: (primeiro_numero * segundo_numero)
    dividir = lambda v1, v2: (
        (primeiro_numero / segundo_numero)
        if segundo_numero != 0
        else "Erro: Divisão por zero."
    )

    primeiro_numero = float(input("Informe o primeiro número: "))
    segundo_numero = float(input("Informe o segundo número: "))
    operador = input("Escolha a operação (|+|-|*|/|): ")

    # if operador == "+":
    #     return somar(primeiro_numero, segundo_numero)
    # elif operador == "-":
    #     return subtrair(primeiro_numero, segundo_numero)
    # elif operador == "*":
    #     return multiplicar(primeiro_numero, segundo_numero)
    # elif operador == "/":
    #     return dividir(primeiro_numero, segundo_numero)
    # else:
    #     print("Operação inválida!")

    # alternativa para o uso de if e else. Criando um dicionário que vincula o valor do operador digitado com a função designada.
    operacoes = {"+": somar, "-": subtrair, "*": multiplicar, "/": dividir}

    if operador in operacoes:
        # retorna a operação entre o primeiro e o segundo valor
        return operacoes[operador](primeiro_numero, segundo_numero)
    else:
        print("Operação inválida")


def main():
    print(f"O resultado da operação foi: {calcular()}")


if __name__ == "__main__":
    main()
