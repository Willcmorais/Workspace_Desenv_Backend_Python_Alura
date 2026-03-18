import os


def limpar_tela() -> None:
    """Pausa a execução e limpa a tela do terminal."""
    input("\nPressione 'Enter' para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


# -> é um TypeHunting. Quer dizer que documentalmente eu devo receber dois floats e retornar um outro float também
def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("[Erro] Impossível dividir por zero.")
    return a / b


def obter_dados_usuario() -> tuple[str, float, float]:
    operacoes_validas = ("+", "-", "*", "/")

    while True:
        print(f"Operadores disponíveis: {operacoes_validas}\n")
        operador = input("Informe a operação que deseja utilizar: ")

        if operador not in operacoes_validas:
            print("Digite apenas as operações disponíveis.")
            limpar_tela()
            continue
        break

    while True:
        try:
            primeiro_numero = float(input("Informe o primeiro número: "))
            segundo_numero = float(input("Informe o segundo número: "))
        except ValueError:
            print("Digite apenas números válidos.\n")
            continue
        break

    # Retorna as 3 variáveis validadas de uma só vez (isso forma uma Tupla)
    return operador, primeiro_numero, segundo_numero


def calcular_resultado(operador: str, n1: float, n2: float) -> float:
    match operador:
        case "+":
            return somar(n1, n2)
        case "-":
            return subtrair(n1, n2)
        case "*":
            return multiplicar(n1, n2)
        case "/":
            return dividir(n1, n2)


def mostrar_resultado() -> None:
    operador, primeiro_numero, segundo_numero = obter_dados_usuario()

    try:
        resultado = calcular_resultado(operador, primeiro_numero, segundo_numero)
        print(
            f"\nResultado: {primeiro_numero} {operador} {segundo_numero} = {resultado:.2f}"
        )
    except ZeroDivisionError:
        print(f"\n[Erro] Não é possível dividir por zero.")
