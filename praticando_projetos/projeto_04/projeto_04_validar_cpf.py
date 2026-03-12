def validar_cpf(cpf):
    if not cpf.isdigit():
        return print("Erro: O CPF deve conter apenas números.")
    if len(cpf) != 11:
        return print("Erro: O CPF deve ter exatamente 11 dígitos.")
    return print("CPF válido.")
