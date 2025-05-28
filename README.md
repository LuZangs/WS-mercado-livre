# 🚗 Web Scraping de Chevrolet Astra no Mercado Livre

Este projeto realiza o scraping de anúncios do carro **Chevrolet Astra** no site **Mercado Livre**, coletando os títulos, preços e links de veículos com valores abaixo de **R$ 30.000**.

## 🔧 Tecnologias utilizadas

- Python 3
- BeautifulSoup (bs4)
- requests
- pandas (opcional, para exportação)

## 📦 Requisitos

Antes de rodar o script, instale os pacotes necessários com:

```bash
pip install beautifulsoup4 requests pandas
```
▶️ Como executar

Clone o repositório:
```
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```
Execute o script:
```
python scraping_astra.py
```
✅ Funcionalidades
Busca de veículos do tipo Chevrolet Astra

Filtro por preço (menores que R$ 30.000)

Exibição no terminal (título, preço e link)

Exportação para CSV (opcional)

📌 Observações
As classes HTML do Mercado Livre podem mudar com o tempo. Mantenha o código atualizado conforme necessário.

O script realiza scraping de apenas uma página. Para múltiplas páginas, é necessário adaptação.

📤 Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias!




