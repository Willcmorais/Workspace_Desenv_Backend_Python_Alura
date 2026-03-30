# Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.
# Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.


class Escola:
    def __init__(self, nome_escola):
        self._nome_escola = nome_escola
        self._notas = [10, 3, 5, 9.8, 5.5, 3.4, 10, 6.6, 7.1, 9.1, 9, 4, 2.5]

    def organizar_notas(self):
        self._notas.sort()
        print(f"--- Notas da instituição de ensino {self._nome_escola} ---")
        for nota in self._notas:
            print(f"{nota:.1f}")
