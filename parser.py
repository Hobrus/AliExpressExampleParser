import requests
import pandas as pd
from bs4 import BeautifulSoup

names = []
prices = []
urls = []
for i in range(1, 6):
    answer = requests.get(f"https://aliexpress.ru/wholesale?SearchText=iphone+14%20pro%20128&page={i}")

    soup = BeautifulSoup(answer.text, 'html.parser')

    iphones = soup.find_all("div", {"class": "product-snippet_ProductSnippet__content__1ettdy"})

    for iphone in iphones:
        name = iphone.find("div", {"class": "product-snippet_ProductSnippet__name__1ettdy"})
        price = iphone.find("div", {"class": "snow-price_SnowPrice__mainM__18x8np"})
        url = iphone.find("a", {"class": "product-snippet_ProductSnippet__galleryBlock__1ettdy"})
        new_price = price.text[:-8]
        new_price = new_price.replace(chr(160), '')
        if int(new_price) > 45000:
            names.append(name.text)
            prices.append(int(new_price))
            urls.append('https://aliexpress.ru'+url['href'])

df = pd.DataFrame()
df['names'] = names
df['prices'] = prices
df['urls'] = urls
df.to_excel('result.xlsx')