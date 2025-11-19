# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]


def converter_telefones(telefones):
    telefones_convertidos = list(map(lambda tel: int(tel), telefones))
    return telefones_convertidos


def verificar_tipos(telefones):
    for numeros in telefones:
        if isinstance(numeros, int):
            return "Todos os números foram convertidos para inteiro!"
        else:
            return "Os números não foram convertidos para inteiro!"


def main():
    print(f"listagem original: {telefones}")

    lista_convertida_int = converter_telefones(telefones)
    print(f"Listagem convertida para inteiros: {lista_convertida_int}")

    validacao = verificar_tipos(lista_convertida_int)
    print(validacao)


if __name__ == "__main__":
    main()
