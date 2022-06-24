import requests
from bs4 import BeautifulSoup


def get_value(target):
    URL = f'https://finance.yahoo.com/quote/{target}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    product = soup.find('div', {"id": "mrt-node-Lead-4-QuoteHeader"})
    value = product.find('fin-streamer', {"data-field": "regularMarketPrice", "data-pricehint": "2"})["value"]
    change = product.find('fin-streamer', {"data-field": "regularMarketChange", "data-pricehint": "2"})["value"]
    change_pct = product.find('fin-streamer',
                              {"data-field": "regularMarketChangePercent", "data-pricehint": "2"})["value"]
    return value, change, change_pct


print(get_value("ETH-USD"))
