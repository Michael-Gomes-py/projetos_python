import requests

#url da API

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

#faz a requisição para a API

requisicao = requests.get(url)

#converte a resposta para json

dados = requisicao.json()

#acessa os dados do dolar 

moeda = dados ["USDBRL"]

#obter as informações

nome = ["name"]
bid = moeda["bid"]
ask = moeda["ask"]
variacao = moeda["pctChange"]

#exibe os resultados

print("=" *40)

print(" COTAÇÃO DO DOLAR")

print("=" *40)

print(f"Moeda: {nome} ")
print(f"BID: R$ {bid} ")
print(f"ASK: R$ {ask} ")
print(f"Variação: {variacao}% ")

print("=" *40)