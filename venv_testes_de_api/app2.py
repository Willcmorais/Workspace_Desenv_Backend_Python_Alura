import requests
import json

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()

for conversao, dados in dados_json.items():
    codigo_moeda = dados["code"]
    codigo_moeda_ref = dados["codein"]
    nome_moeda = dados["name"]
    val_mais_alto = float(dados["high"])
    val_mais_baixo = float(dados["low"])
    variacao_lance = float(dados["varBid"])
    percentual_mudanca = float(dados["pctChange"])
    preco_compra = float(dados["bid"])
    preco_venda = float(dados["ask"])

    print(
        f"==== {conversao} ====\nCódigo da moeda: {codigo_moeda}\nCódigo da moeda de referência: {codigo_moeda_ref}\nNome da moeda: {nome_moeda}\nValor mais alto: {val_mais_alto:.2f}\nValor mais baixo: {val_mais_baixo:.2f}\nVariação do lance: {variacao_lance:.2f}\nPecentual de mudança: {percentual_mudanca:.2f}\nPreço de compra: {preco_compra:.2f}\nPreço de venda: {preco_venda:.2f}\nCarimbo da data/hora: {dados["timestamp"]}\nData e hora do registro: {dados["create_date"]}"
    )
