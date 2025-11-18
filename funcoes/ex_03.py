# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

# Se for antes das 12h, exibir "Bom dia";
# Entre 12h e 18h, exibir "Boa tarde";
# Após 18h, exibir "Boa noite".


def saudar(hora_atual):
    if hora_atual < 12:
        return "Bom dia!"
    elif 12 <= hora_atual <= 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"


def main():
    hora_atual = int(input("Informe a hora atual: "))
    print(saudar(hora_atual))


if __name__ == "__main__":
    main()
