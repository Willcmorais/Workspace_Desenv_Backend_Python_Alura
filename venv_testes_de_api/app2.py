import requests
import json

url = "https://economia.awesomeapi.com.br/last/BRL-ARS"
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()

for conversao, dados in dados_json.items():
    print(
        f"==== {conversao} ====\nCódigo da moeda: {dados["code"]}\nCódigo da moeda de referência: {dados["codein"]}\nNome da moeda: {dados["name"]}\nValor mais alto: {dados["high"]}\nValor mais baixo: {dados["low"]}\nVariação do lance: {dados["varBid"]}\nPecentual de mudança: {dados['pctChange']}\nPreço de compra: {dados["bid"]}\nPreço de venda: {dados["ask"]}\nCarimbo da data/hora: {dados["timestamp"]}\nData e hora do registro: {dados["create_date"]}"
    )
