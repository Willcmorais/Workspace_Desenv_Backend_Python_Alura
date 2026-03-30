from registrador_voluntarios import Registrador


def main():
    app = Registrador()

    app.adicionar_voluntario()

    print()
    app.listar_voluntarios()


if __name__ == "__main__":
    main()
