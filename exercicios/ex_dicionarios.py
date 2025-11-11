# Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
infos_pessoa = {'nome': 'William', 'idade': 28, 'cidade': 'Recife'}
print(infos_pessoa)

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
infos_pessoa['idade'] = 29
print(infos_pessoa)

# Adicione um campo de profissão para essa pessoa;
infos_pessoa['profissao'] = 'Programador'
print(infos_pessoa)

# Remova um item do dicionário.
infos_pessoa.pop('profissao')
print(infos_pessoa)

# Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
dicionario_exemplo = {1: 'William', 2: 'Maria', 3: 'Victoria', 4: 'Ana', 5: 'Manoel'}
print(dicionario_exemplo)

# Verifique se uma chave específica existe dentro desse dicionário.
verificando_chave = int(input('Informe o número da chave que deseja achar: '))
print(f'A chave {verificando_chave} foi encontrada no dicionário.') if verificando_chave in dicionario_exemplo.keys() else print(f'a chave {verificando_chave} não foi encontrada no dicionário.')

# Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = 'O bem que fazemos é o bem que recebemos, e esse bem faz bem.'
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)