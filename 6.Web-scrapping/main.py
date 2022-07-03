import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

# определяем список ключевых слов
KEYWORDS = ['сети', 'raspberry pi', 'web', 'python']
MAIN_LINK = 'https://habr.com/ru/all'

headers = Headers(os='win', headers=True).generate()
ret = requests.get(MAIN_LINK, headers=headers)

soup = BeautifulSoup(ret.text, 'html.parser')
articles = soup.findAll("article", {"class": "tm-articles-list__item"})

article_dicts = []
for article in articles:
	# смотрим совпадение по ключевым словам
	hubs = article.findAll("a", {"class": "tm-article-snippet__hubs-item-link"})
	key_words = [hub.span.text.lower() for hub in hubs]
	is_match = False
	matching = [words for words in key_words for key in KEYWORDS if key in words]
	if len(matching):
		is_match = True

	if is_match:
		title = article.find("a", {"class": "tm-article-snippet__title-link"})
		date = article.find("span", {"class":"tm-article-snippet__datetime-published"})
		article_dicts.append({
			"title":title.span.text, 
			"ref":MAIN_LINK+title["href"],
			"datetime":date.time["datetime"],
			"matching":matching
			})


for article in article_dicts:
	print(f"{article['datetime']} - {article['title']} - {article['ref']}")
	print(f"matched words: {article['matching']}")
	print()
