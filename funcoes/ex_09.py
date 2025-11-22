# Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras. Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.


def criar_desconto(valor_compra):
    def calcular_preco(porcentagem_desconto):
        resultado = valor_compra - (valor_compra * (porcentagem_desconto / 100))
        return resultado

    return calcular_preco


def main():
    valor_produto = float(input("Informe o valor do produto(R$): "))
    porcentagem_desconto = float(input("Informe o desconto(%): "))

    valor_produto = criar_desconto(valor_produto)
    calculo_desconto = valor_produto(porcentagem_desconto)

    print(f"Preço final com desconto: {calculo_desconto}")


if __name__ == "__main__":
    main()
