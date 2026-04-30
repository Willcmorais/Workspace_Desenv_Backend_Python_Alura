# Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

permissoes_principais = set(
    p.strip()
    for p in input("\nPermissões principais(separadas por vírgula): ")
    .lower()
    .split(",")
)

permissoes_solicitadas = set(
    p.strip()
    for p in input("\nPermissões solicitadas(separadas por vírgula): ")
    .lower()
    .split(",")
)

eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais)

if eh_subconjunto:
    print("\nAs permissões solicitadas fazem parte das permissões principais.")
else:
    print("\nAs permissões solicitadas NÃO fazem parte das permissões principais.")


# permissoes_do_sistema = set(["leitura", "escrita", "execução", "compartilhamento"])

# permissoes_solicitadas = set(
#     input("Informe as permissões(separadas por vírgula): ").lower().split(", ")
# )

# permissao_diferente = permissoes_solicitadas.difference(permissoes_do_sistema)

# if permissao_diferente:
#     print("As permissões solicitadas NÃO fazem parte das permissões principais.")
#     print(permissao_diferente)
# else:
#     print("As permissões solicitadas fazem parte das permissões principais.")
#     print(permissao_diferente)
