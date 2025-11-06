# Importando o os podemos utilizar a função de limpar o terminal quando quisermos
import os

# Aqui vamos criar as nossas variáveis, neste caso será um dicionário para armazenar as informações dos restaurantes com seus dados
restaurantes = [['Pizzaloka', 'Pizza', 'William'], ['Sushibar Lounge', 'Sushi', 'Victoria']]

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

    restaurantes.append([nome_restaurante, categoria_restaurante, nome_proprietario_restaurante])

    print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!')
    
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listagem de restaurantes cadastrados:')
    
    for restaurante in restaurantes:
        print(f'. {restaurante}')

    voltar_ao_menu()

def ativar_novo_restaurante():
    exibir_subtitulo('Hora de ativar o seu restaurante!')
    
    voltar_ao_menu()

def opcao_invalida():
    exibir_subtitulo("Opção Inválida!")
    
    voltar_ao_menu()

def encerrar_programa():
    exibir_subtitulo('Encerrando programa...')

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_novo_restaurante()
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
