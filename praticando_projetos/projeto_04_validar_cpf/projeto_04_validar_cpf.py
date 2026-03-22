import os


def limpar_tela():
    input("\nPressione 'Enter' para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


def validar_cpf():
    while True:
        try:
            cpf = int(input("Informe os dígitos do seu CPF: "))
        except ValueError:
            print("Digite apenas números inteiros.")
            limpar_tela()
            continue

        cpf = str(cpf)
        cpf = list(cpf)

        if len(cpf) != 11:
            return "Erro: O CPF deve ter exatamente 11 dígitos."
        return "CPF válido."


def main():
    print(validar_cpf())
