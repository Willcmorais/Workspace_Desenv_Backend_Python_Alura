# Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras. Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.


def criar_desconto(porcentagem_desconto):  # Recebe o desconto fixo
    def calcular_preco(valor_compra):  # Recebe o valor do produto depois
        resultado = valor_compra - (valor_compra * (porcentagem_desconto / 100))
        return resultado

    return calcular_preco  # Retorna a função que "lembra" do desconto


def main():
    # Exemplo prático do poder da Closure:
    # Criamos duas funções "especializadas" usando a mesma fábrica
    cupom_black_friday = criar_desconto(20)  # Essa função sempre tirará 20%
    cupom_primeira_compra = criar_desconto(10)  # Essa função sempre tirará 10%

    # Agora aplicamos os cupons em produtos com valores diferentes
    print(f"Produto de R$100 na Black Friday: R${cupom_black_friday(100):.2f}")
    print(f"Produto de R$200 na Black Friday: R${cupom_black_friday(200):.2f}")
    print(f"Produto de R$100 na Primeira Compra: R${cupom_primeira_compra(100):.2f}")


if __name__ == "__main__":
    main()
