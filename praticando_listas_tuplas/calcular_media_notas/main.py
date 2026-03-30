# A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.

notas_str = input("Informe as notas da turma separadas por vírgula: ").split(",")
print(f"Lista de notas no formato string:\n{notas_str}")

notas_float = []

for nota in notas_str:
    notas_float.append(float(nota))

print(f"\nLista de notas no formato float:\n{notas_float}")

media = sum(notas_float) / len(notas_float)
print(f"\nMédia das notas: {media:.2f}")
