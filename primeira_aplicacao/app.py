# Importando a biblioteca 'os' podemos utilizar a função de limpar o terminal quando quisermos
import os

# Variáveis, neste caso será um dicionário para armazenar as informações dos restaurantes com seus dados
restaurantes = [
    {
        "nome": "Pizzaloka",
        "categoria": "Pizza",
        "proprietario": "William",
        "ativo": True,
    },
    {
        "nome": "Sushibar Lounge",
        "categoria": "Sushi",
        "proprietario": "Victoria",
        "ativo": False,
    },
    {
        "nome": "Cantina da Ana",
        "categoria": "Brasileira",
        "proprietario": "Ana Maria",
        "ativo": False,
    },
]


# Funções são utilizadas para deixar o código mais limpo, e quando necessário alguma alteração, podemos fazer isso apenas na função e não nas condicionais
def exibir_nome_programa():
    """Esta função vai exibir o nome do programa para o usuário.
    
    Outputs:
    - Título do app.
    """

    print("---------------------------------------------------------")
    print("=============Ｓａｂｏｒｅｓ Ｄｉｖｅｒｓｏｓ=============")
    print("---------------------------------------------------------\n")


def exibir_opcoes():
    """Esta função vai exibir as opções do programa para o usuário
    
    Outputs:
    - Opções do app para o usuário.
    """

    print("1. Cadastrar novo restaurante.")
    print("2. Listar restaurantes.")
    print("3. Ativar/desativar restaurante.")
    print("4. Sair.\n")


def cadastrar_novo_restaurante():
    """Esta função é para cadastrar novos restaurantes. Solicitando o nome, categoria e proprietário. Ele sempre inicia como inativo.
    
    Inputs:
    - Nome do restaurante;
    - Categoria do restaurante;
    - Nome do proprietário.
    
    Outputs:
    - Adiciona todas as informações dos inputs para um novo dicionário na lista;
    - Caso o cadastro tenha sido finalizado, mostra mensagem de sucesso na tela com o nome do restaurante;
    - volta ao menu principal.
    """

    exibir_subtitulo("Área de cadastro para novos restaurantes:")

    nome_restaurante = input("Informe aqui o nome do seu restaurante: ")
    categoria_restaurante = input(
        "Informe aqui o tipo de comida que seu restaurante oferece: "
    )
    nome_proprietario_restaurante = input(
        "Informe aqui o nome do proprietário do restaurante: "
    )

    restaurantes.append(
        {
            "nome": nome_restaurante,
            "categoria": categoria_restaurante,
            "proprietario": nome_proprietario_restaurante,
            "ativo": False,
        }
    )

    print(f"\nRestaurante {nome_restaurante} cadastrado com sucesso!")

    voltar_ao_menu()


def listar_restaurantes():
    """Esta função vai listar os restaurantes cadastrados no formato de tabela com o nome, categoria, proprietário e o status. Está tudo justificado
    
    Outputs:
    - Exibe o subtítulo da função;
    - Exibe as informações dos restaurantes já cadastrados em forma de tabela justificada;
    - Volta ao menu principal.
    """

    exibir_subtitulo("Listagem de restaurantes cadastrados:")

    print(
        "Nome do restaurante:".ljust(22),
        "Categoria:".ljust(22),
        "Proprietário(a):".ljust(22),
        "Ativo:"
    )

    for restaurante in restaurantes:
        print(
            f"- {restaurante['nome']:<{20}} | {restaurante['categoria']:<{20}} | {restaurante['proprietario']:<{20}} | {restaurante['ativo']}"
        )
    voltar_ao_menu()


def alternar_estado_restaurante():
    """Esta função vai alternar o status de ativado ou desativado dos restaurantes. Caso o restaurante esteja ativo ele vai desativar, e vice versa. Caso o restaurante esteja desativado e tentemos desativar ele vai mostrar a mensagem de erro, e vice versa.
    
    Inputs:
    - Nome do restaurante;
    - Alternar o estado do restaurante(ativado, desativado).
    
    Outputs:
    - Mensagens de sucesso para restaurantes ativados ou desativados
    - Mensagens de erro para restaurantes já ativados que tentaram ser ativados ou desativados que tentaram ser desativados;
    - Volta ao menu principal.
    """

    exibir_subtitulo("Ative ou desative seu restaurante aqui!")

    nome_restaurante = input("Informe o nome do seu restaurante: ")

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            alternar_estado_restaurante = int(
                input("\nDigite 0 para desativar ou 1 para ativar: ")
            )

            if alternar_estado_restaurante == 0 and restaurante["ativo"] == True:
                restaurante["ativo"] = False
                print(
                    f"\nO restaurante {restaurante['nome']} foi desativado com sucesso."
                )
            elif alternar_estado_restaurante == 1 and restaurante["ativo"] == False:
                restaurante["ativo"] = True
                print(f"\nO restaurante {restaurante['nome']} foi ativado com sucesso.")
            elif alternar_estado_restaurante == 0 and restaurante["ativo"] == False:
                print("\nNão é possível desativar restaurante, ele já está desativado.")
            else:
                print("\nNão é possível ativar restaurante, ele já está ativo.")
        else:
            opcao_invalida()
        break
    voltar_ao_menu()


def opcao_invalida():
    """Esta função vai mostrar uma mensagem de opção inválida sempre que o usuário der um input fora dos padrões estabelecidos."""

    exibir_subtitulo("Opção Inválida!")

    voltar_ao_menu()


def encerrar_programa():
    """Esta função vai simplesmente mostrar o subtítulo de encerrar o programa quando o usuário escolher a opção."""

    exibir_subtitulo("Encerrando programa...")


def escolher_opcao():
    """Esta função vai selecionar a opção escolhida de acordo com o que o usuário digitar no input, chamando assim as outras funções já estabelecidas."""

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                encerrar_programa()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

    # if opcao_escolhida == 1:
    #     cadastrar_restaurante()
    # elif opcao_escolhida == 2:
    #     listar_restaurante()
    # elif opcao_escolhida == 3:
    #     ativar_restaurante()
    # else:
    #     encerrar_programa()


def voltar_ao_menu():
    """Esta função vai retornar ao menu quando o usuário finalizar todos os passos que desejar de uma tarefa e apertar a tecla solicitada."""

    print()
    input("Pressione Enter para voltar ao menu principal ")
    main()


def exibir_subtitulo(texto):
    """Esta função vai exibir os subtítulos nas outras funções, economizando prints. Vai mostrar também com uma personalização de asteriscos pulando linhas e apagando o que foi feito anteriormente no terminal."""

    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def main():
    """A função main é a função principal do programa, sempre vai ser rodada chamando as outras funções de acordo com o que o usuário escolher nas opções iniciais."""

    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
