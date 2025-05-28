from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/chevrolet/astra"
headers = {"User-Agent": "Mozilla/5.0"}

pagina = requests.get(url, headers=headers)
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

produtos = dados_pagina.find_all('div', class_="ui-search-result__wrapper")

for div in produtos:
    titulo_tag = div.find('a', class_="poly-component__title")
    preco_tag = div.find('span', class_="andes-money-amount__fraction")
    if titulo_tag and preco_tag:
     titulo = titulo_tag.text.strip()
     preco = preco_tag.text.strip()
     link = titulo_tag.get('href')
     preco_limpo = preco.replace("R$", "").replace(".", "").strip()
     preco_numerico = int(preco_limpo)

    if titulo_tag and preco_numerico < 30000:  
     print(f"🟢 Título: {titulo}")
     print(f"💰 Preço: R$ {preco}")
     print(f"🔗 Link: {link}")
     print("-" * 60)
    