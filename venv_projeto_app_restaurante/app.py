# Importa a biblioteca responsável por fazer requisições HTTP (como se o Python estivesse "navegando" no seu navegador).
import requests

# Importa a biblioteca para manipular o formato JSON, que é o padrão de troca de dados na web.
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

# O Python envia um "Ei, me mande os dados!" para o servidor. O servidor responde com um objeto que guardamos em response.
response = requests.get(url)
# Geralmente vai imprimir <Response [200]>. O código 200 significa que a conexão foi um sucesso.
print(response)

# Só prossegue se o site respondeu corretamente.
if response.status_code == 200:
    # Transforma o texto bruto que veio da internet em uma lista de dicionários do Python.
    dados_json = response.json()
    # Cria um dicionário vazio que usaremos para organizar as coisas: a chave será o nome do restaurante e o valor será uma lista de pratos.
    dados_restaurante = {}

    # Percorre cada prato da lista gigante.
    for item in dados_json:
        # Criar uma variável com o nome do restaurante
        nome_do_restaurante = item["Company"]

        # Se é a primeira vez que vemos esse restaurante, criamos uma "gaveta" (lista vazia) para ele no nosso dicionário.
        if nome_do_restaurante not in dados_restaurante:
            # Cria uma lista
            dados_restaurante[nome_do_restaurante] = []

        # Adiciona as informações do prato (nome, preço, descrição) dentro da gaveta do restaurante correspondente.
        dados_restaurante[nome_do_restaurante].append(
            {
                "item": item["Item"],
                "preco": item["price"],
                "descricao": item["description"],
            }
        )
else:
    print(f"O erro foi {response.status_code}")

# Percorre nosso dicionário organizado, pegando o nome do restaurante e a lista de pratos de cada um.
for nome_do_restaurante, dados in dados_restaurante.items():
    # Cria o nome do arquivo (ex: McDonalds.json).
    nome_do_arquivo = f"{nome_do_restaurante}.json"

    # Abre (ou cria) o arquivo no modo de escrita (write). O with garante que o arquivo seja fechado automaticamente depois.
    with open(nome_do_arquivo, "w") as arquivo_restaurante:
        # Pega a lista de pratos e escreve dentro do arquivo no formato JSON. O indent=4 serve para o arquivo ficar mais legível para humanos, com espaços e quebras de linha.
        json.dump(dados, arquivo_restaurante, indent=4)
