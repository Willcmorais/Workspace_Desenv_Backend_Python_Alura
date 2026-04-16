import requests
import json

# realizar a requisição para api
url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)

# verificar o statuscode, processar os dados, organizar as informações por restaurante
if response.status_code == 200:
    print(response)
    dados_restaurante = {}
    dados_json = response.json()

    for item in dados_json:
        nome_restaurante = item["Company"]

        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append(
            {
                "produto": item["Item"],
                "preco": item["price"],
                "descricao": item["description"],
            }
        )
else:
    print(response)

# # salvar os dados em um aruivos JSON individual
# for nome_restaurante, dados in dados_restaurante.items():
#     nome_arquivo = f"{nome_restaurante}.json"

#     with open(nome_arquivo, "w") as arquivo_restaurante:
#         json.dump(dados, arquivo_restaurante, indent=4)
# else:
#     print(response)
