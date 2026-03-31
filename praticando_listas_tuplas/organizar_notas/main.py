class Colegio:
    def __init__(self):
        self._notas = []

    def adicionar_nota(self):
        entrada = input("Informe as notas separadas por vígula: ")

        # Converte para float e cria a lista em uma linha só
        novas_notas = [float(nota.strip()) for nota in entrada.split(",")]

        # Adiciona todos os elementos de uma vez à lista principal
        self._notas.extend(novas_notas)

    def organizar_notas(self):
        # Como o sort retorna um None não precisamos do return, apenas utilizar a função para exercer a ação
        self._notas.sort()

    def mostrar_notas(self):
        print("\n--- Notas em Ordem Crescente ---")
        if not self._notas:
            print("Nenhuma nota cadastrada.")
        for nota in self._notas:
            print(f"- {nota:.2f}")  # Formatado com 2 casas decimais


def main():
    colegio = Colegio()
    colegio.adicionar_nota()
    colegio.organizar_notas()
    colegio.mostrar_notas()


if __name__ == "__main__":
    main()
