import os


def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu() -> None:
    limpar_tela()
    print("**** BEM VINDO AO ATM ****")
    print("Cédulas disponíveis para saque:\n")
    print(". R$ 2,00\n. R$ 5,00\n. R$ 10,00\n. R$ 50,00\n. R$ 100,00\n")


def solicitar_saque() -> int:
    # Tipos de saques não aceitos
    saques_indisponiveis = [0, 1, 3]
    ultimo_digito = ["1", "3"]

    while True:
        try:
            # Solicita o valor ao usuário
            saque_solicitado = int(input("Informe o valor do saque: "))

            # Manipula o valor solicitado de inteiro para transformar em uma string e depois para uma lista. Caso seja necessário comparar o último dígito do valor solicitado.
            saque_solicitado_str = str(saque_solicitado)
            saque_solicitado_str = list(saque_solicitado_str)

            # Saques de 0, 1 ou 3 não são aceitos
            if saque_solicitado in saques_indisponiveis:
                print(
                    "Não temos saques disponíveis para R$ 0.00, R$ 1.00 e R$ 3.00. Informe um valor diferente.\n"
                )
                continue
            # Aqui utilizamos a manipulação do valor inputado transformado em lista para verificar se o último digito é igual a 1 ou 3. Valores nesse formato não são aceitos.
            elif saque_solicitado_str[-1] in ultimo_digito:
                print(
                    "Impossível sacar valores finalizados em 1 e 3. Tente outro valor.\n"
                )
                continue
        # Se a informação não for algo diferente de um dígito, não será aceito
        except ValueError:
            print("Digite apenas números inteiros.\n")
            continue
        # Retorna o valor no formato original(inteiro)
        return saque_solicitado


def contar_notas(saque_solicitado: int) -> dict:
    # Cédulas disponíveis para saque
    cedulas_disponiveis = [100, 50, 20, 10, 5, 2]
    # Dicionário para guardar a cédula e a quantidade
    cedulas_selecionadas = {}

    # Vai percorrer todas as cédulas, iniciando pelo 100.
    for cedula in cedulas_disponiveis:
        # Quantas notas desse valor cabem no montante do saque solicitado
        qntd_de_notas = saque_solicitado // cedula

        # Se a quantidade de notas que cabem no saque for > 1, então será adicionado ao dicionário a nota e a quantidade.
        if qntd_de_notas > 0:
            cedulas_selecionadas[cedula] = qntd_de_notas

            # Atualizamos o valor restante pegando apenas o "resto" da divisão e voltamos para o loop até finalizar todo o valor
            saque_solicitado = saque_solicitado % cedula

    return cedulas_selecionadas


def main():
    mostrar_menu()

    # Variável que vai receber o valor da solicitação do saque
    saque_solicitado = solicitar_saque()

    # A função contar notas vai pegar o valor da solicitação, calcular e retornar esse valor, no formato de dicionário, para a variável
    notas_selecionadas = contar_notas(saque_solicitado)

    limpar_tela()

    # Vamos printar a mensagem final do valor solicitado com todas as notas selecionadas
    print(
        f"Seu saque de R$ {saque_solicitado:.2f} já está sendo processado...\n\nVocê vai receber:\n"
    )
    # Para cada nota e quantidade de notas nas notas selecionadas vai printar as quantidades e as notas
    for cedula, qntd_notas in notas_selecionadas.items():
        print(f"-> {qntd_notas} nota(s) de R$ {cedula:.2f}")

    print("\nAgradecemos a preferência. Volte sempre!")
