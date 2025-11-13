# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.

# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

# Crie um programa que implemente essa lógica usando um laço while.


def cadastrar_user():
    while True:
        nome_usuario = input("Digite seu nome de usuário: ")
        senha_usuario = input("Digite sua senha: ")

        if len(nome_usuario) < 5:
            print("O nome de usuário deve ter pelo menos 5 caracteres.")
            continue

        if len(senha_usuario) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
            continue

        print("Cadastro realizado com sucesso!")
        break


def main():
    cadastrar_user()


if __name__ == "__main__":
    main()
