# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.

# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

# Crie um programa que implemente essa lógica usando um laço while.


def cadastrar_user():
    nome_user = ""
    senha_user = ""

    while len(nome_user) < 5 and len(senha_user) < 8:
        nome_user = input("Informe seu nome de usuário(mínimo de 5 caracteres): ")
        senha_user = input("Informe a sua senha(mínimo de 8 caracteres): ")


def main():
    cadastrar_user()


if __name__ == "__main__":
    main()
