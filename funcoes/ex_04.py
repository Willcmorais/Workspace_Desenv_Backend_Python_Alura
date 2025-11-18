# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]


def converter_string_int(telefones):
    numeros = list(map(lambda tel: int(tel), telefones))
    return numeros


def validar_conversao_int():
    return lambda tel: tel == int, telefones


def main():
    print(
        f"Lista de strings convertida para inteiros: {converter_string_int(telefones)}"
    )

    print(f"A conversão da lista está {validar_conversao_int()}")


if __name__ == "__main__":
    main()
