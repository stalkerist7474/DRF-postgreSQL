import os
import requests
from bs4 import BeautifulSoup
from pathlib import Path



#base = 'https://www.220-volt.ru/catalog/lampy/'
base = 'https://www.electro-mpo.ru/catalog/lampy_elektropatrony/'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
#print(soup)

div = soup.find('div', class_='s-products-list')

#print(div)

url_news_html = div.find_all('div', class_='s-products__item__wrapper')
#print(url_news_html)

for a in url_news_html:
    link_news = a.find('a').get('href')


print(link_news)