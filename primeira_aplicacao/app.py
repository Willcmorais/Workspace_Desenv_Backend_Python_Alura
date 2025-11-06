# Importando o os podemos utilizar a função de limpar o terminal quando quisermos
import os

# Aqui vamos criar as nossas variáveis, neste caso será um dicionário para armazenar as informações dos restaurantes com seus dados
restaurantes = [['Pizzaloka', 'Pizza', 'William'], ['Sushibar Lounge', 'Sushi', 'Victoria']]

# Funções são utilizadas para deixar o código mais limpo, e quando necessário alguma alteração, podemos fazer isso apenas na função e não nas condiconais
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
    os.system('cls')
    print('Hora de cadastrar o seu restaurante!\n')
    
    nome_restaurante = input("Informe aqui o nome do seu restaurante: ")
    categoria_restaurante = input("Informe aqui o tipo de comida que seu restaurante oferece: ")    
    nome_proprietario_restaurante = input("Informe aqui o nome do proprietário do restaurante: ")

    restaurantes.append([nome_restaurante, categoria_restaurante, nome_proprietario_restaurante])
    
    print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!')
    
    input('\nPressione Enter para voltar ao menu principal.')
    main()

def listar_restaurantes():
    os.system("cls")
    print('Lista de restaurantes cadastrados:\n')
    for restaurante in restaurantes:
        print(f'. {restaurante}')

    input("\nPressione Enter para voltar ao menu principal.")
    main()

def ativar_novo_restaurante():
    print('Hora de ativar o seu restaurante!')

def encerrar_programa():
    os.system("cls")
    print("Encerrando programa...\n")

def opcao_invalida():
    print('Opção inválida!\n')
    input('Pressione Enter para voltar ao menu principal.')
    main()

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

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
