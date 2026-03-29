# Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar. Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.


class Registrador:
    def __init__(self):
        self._lista_voluntarios = []

    def adicionar_voluntario(self):
        while True:
            self._nome_voluntario = (
                input("Informe o nome do voluntário ou digite 'Sair': ").strip().title()
            )

            if self._nome_voluntario == "Sair":
                break
            if self._nome_voluntario:
                self._lista_voluntarios.append(self._nome_voluntario)

    def listar_voluntarios(self):
        print("--- Lista de voluntários ---\n")
        if not self._lista_voluntarios:
            print("Nenhum voluntário registrado.")
        else:
            for voluntario in self._lista_voluntarios:
                print(f"- {voluntario}")
