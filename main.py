from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

html = urlopen('https://habr.com/ru/search/?q=crypto+wallet+security&target_type=posts&order=relevance')
bs = BeautifulSoup(html, "html.parser")

articles = bs.findAll('article', {'class': 'tm-articles-list__item'})

article_list = []
for article in articles:
    user_name = article.find('a', {'class': 'tm-user-info__username'}).get_text()
    title = article.find('h2', {'class': 'tm-title tm-title_h2'}).get_text()
    link = article.find('a', {'class': 'tm-title__link'})['href']

    article_data = {
        "title": title,
        "author": user_name,
        "link": f"https://habr.com{link}"
    }
    article_list.append(article_data)

print(json.dumps(article_list, ensure_ascii=False, indent=4))
