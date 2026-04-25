# O fastapi é um módulo e o FastAPI é uma classe desse módulo
import requests
from fastapi import FastAPI, Query

# Precisa dessa linha para dar o "start" na fastapi para utilizar
app = FastAPI()


# @app Refere-se à instância do FastAPI criada. .get define o Método HTTP. O GET é usado justamente quando o navegador (ou cliente) quer "buscar" ou "pedir" uma informação. /api/hello é o Caminho (Path). Se o servidor estiver rodando em localhost:8000, a URL completa para acessar essa função será http://localhost:8000/api/hello.
@app.get("/api/hello")
def hello_world():
    """
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    """

    # Retornar um dicionário faz com que o navegador receba um JSON: {"message": "Hello World!"}
    return {"message": "Hello World!"}


# para rodar esse código utilizamos no cmd a instrução: uvicorn main:app --reload


@app.get("/api/restaurantes/")
# O None diz que esse parâmetro é opcional. Se não passar nada, o código executa o if restaurante is None
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para ver os cardápios dos restaurantes
    """

    # 1. Definimos o 'alvo': a URL da API externa que contém os dados brutos
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    # 2. Fazemos uma requisição GET para essa URL externa usando a biblioteca 'requests'
    response = requests.get(url)

    # 3. Verificamos se a conexão com o servidor externo deu certo (Status 200)
    if response.status_code == 200:
        # Transformamos o texto bruto recebido em um formato que o Python entende (Lista/Dicionário)
        dados_json = response.json()
        # 4. Lógica de Filtro: Se o usuário NÃO passou um nome de restaurante na URL
        if restaurante is None:
            # Retornamos a lista completa de todos os restaurantes
            return {"Dados": dados_json}

        # 5. Se o usuário passou um nome, criamos uma lista vazia para armazenar os resultados filtrados
        dados_restaurante = []

        # Percorremos cada item (prato/restaurante) da lista original
        for item in dados_json:
            # Verificamos se o nome da empresa ("Company") é igual ao que o usuário buscou
            if item["Company"] == restaurante:
                # Se for igual, adicionamos apenas as informações importantes na nossa nova lista
                dados_restaurante.append(
                    {
                        "produto": item["Item"],
                        "preco": item["price"],
                        "descricao": item["description"],
                    }
                )
        # 6. Retornamos o nome do restaurante pesquisado e a lista de itens que encontramos para ele
        return {"Restaurante": restaurante, "Cardapio": dados_restaurante}
    else:
        # Caso a API externa falhe (ex: site fora do ar), avisamos o usuário qual foi o erro
        return {"Erro": f"{response.status_code} - {response.text}"}
