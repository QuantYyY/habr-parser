from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://habr.com/ru/search/?q=crypto+wallet+security&target_type=posts&order=relevance')
bs = BeautifulSoup(html, "html.parser")

articles = bs.findAll('article', {'class': 'tm-articles-list__item'})

for article in articles:
    user_name = article.find('a', {'class': 'tm-user-info__username'}).get_text()
    title = article.find('h2', {'class': 'tm-title tm-title_h2'}).get_text()
    link = article.find('a', {'class': 'tm-title__link'})['href']

    print(title)
    print(f"Автор: {user_name}")
    print(f"https://habr.com{link}")
    print("----------------")