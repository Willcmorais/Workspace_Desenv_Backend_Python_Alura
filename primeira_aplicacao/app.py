# Importando o os podemos utilizar a função de limpar o terminal quando quisermos
import os

# Aqui vamos criar as nossas variáveis, neste caso será um dicionário para armazenar as informações dos restaurantes com seus dados
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
    print("---------------------------------------------------------")
    print("=============Ｓａｂｏｒｅｓ Ｄｉｖｅｒｓｏｓ=============")
    print("---------------------------------------------------------\n")

def exibir_opcoes():
    print("1. Cadastrar novo restaurante.")
    print("2. Listar restaurantes.")
    print("3. Ativar restaurante.")
    print("4. Sair.\n")

def cadastrar_novo_restaurante():
    exibir_subtitulo('Área de cadastro para novos restaurantes:')
    
    nome_restaurante = input("Informe aqui o nome do seu restaurante: ")
    categoria_restaurante = input("Informe aqui o tipo de comida que seu restaurante oferece: ")
    nome_proprietario_restaurante = input("Informe aqui o nome do proprietário do restaurante: ")

    restaurantes.append({'nome': nome_restaurante, 'categoria': categoria_restaurante, 'proprietario': nome_proprietario_restaurante, 'ativo': False})

    print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!')
    
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listagem de restaurantes cadastrados:')

    for restaurante in restaurantes:
        print(f'- Nome: {restaurante['nome']} | Categoria: {restaurante['categoria']} | Proprietário(a): {restaurante['proprietario']} | Ativo: {restaurante['ativo']}.')

    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo('Ative ou desative seu restaurante aqui!')

    nome_restaurante = input('Informe o nome do seu restaurante: ')

    for restaurante in restaurantes:
        if nome_restaurante == restaurante:
            alternar_estado_restaurante = int(input('Digite 0 para desativar ou 1 para ativar: '))

            if alternar_estado_restaurante == 0 and restaurantes['ativo'] == True:
                restaurantes['ativo'] == False
            elif alternar_estado_restaurante == 1 and restaurantes['ativo'] == False:
                restaurantes['ativo'] = True
            elif alternar_estado_restaurante == 0 and restaurantes['ativo'] == False:
                print('Não é possível desativar restaurante, ele já está desativado.')
            else:
                print('Não é possível ativar restaurante, ele já está ativado.')
        else:
            print('Nome do restaurante não encontrado!')
        break

    voltar_ao_menu()

def opcao_invalida():
    exibir_subtitulo('Opção Inválida!')
    
    voltar_ao_menu()

def encerrar_programa():
    exibir_subtitulo('Encerrando programa...')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

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
    print()
    input('Pressione Enter para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
