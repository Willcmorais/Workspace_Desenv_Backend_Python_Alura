# Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).


def calculo_de_imc():
    """
    Esta função vai calcular o IMC do usuário. Recebendo a altura e o peso vai calcular e devolver o IMC.

    Inputs:
    - Peso
    - Altura

    Outputs:
    - Mensagem com o valor do IMC;
    - Se o IMC está acima ou abaixo do normal.
    """

    peso = float(input("Informe o seu peso(kg): "))
    altura = float(input("Informe a sua altura(metros): "))

    imc = peso / altura**2

    print(
        f"Seu IMC foi de {imc:.1f}. Você stá abaixo do peso"
    ) if imc < 18.5 else print(f"Seu IMC foi de {imc:.1f}. Você está acima do peso")


def main():
    calculo_de_imc()


if __name__ == "__main__":
    main()
