def validar_cpf(cpf_do_usuario):
    caracteres = "abcdefghijklmnopqrstuvwxyz,.!|?;:\"'()[]{}"

    for i in len(cpf_do_usuario):
        if cpf_do_usuario[i] == caracteres:
            print("O CPF deve conter apenas números.")
        else:
            if len(cpf_do_usuario) == 11:
                return print("CPF Válido!")
            else:
                print("O CPF deve conter 11 números.")
