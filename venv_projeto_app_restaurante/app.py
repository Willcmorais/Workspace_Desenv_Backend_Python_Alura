# Importar o módulo inteiro das requests
import requests

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

# O response vai buscar para nós, com o verbo do http .get da biblioteca requests, os dados do arquivo json para que possam ser utilizados
response = requests.get(url)
# Aqui ele vai printar apenas o número do status_code da request, se foi feito com sucesso ou deu erro.
print(response)

# O status_code é um range númerico que significa um status da requisição. Por exemplo, o 200 quer dizer que deu certo, já o 404 é que deu erro.
# Aqui queremos dizer que, caso a informação do status_code retorne 200, se a request da response der certo, acessaremos a informação salvando ela em uma variável utilizando outra função do requests que é o .json()
if response.status_code == 200:
    # No arquivo json temos a Company, Item, price e description
    dados_json = response.json()
    dados_restaurante = {}

    for item in dados_json:
        nome_do_restaurante = item["Company"]
        # Se o nome do restaurante(Company) não estiver nos dados do restaurante
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append(
            {
                "item": item["Item"],
                "preco": item["price"],
                "descricao": item["description"],
            }
        )
else:
    print(f"O erro foi {response.status_code}")

print(dados_restaurante["McDonald’s"])
