import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import re
from collections import Counter
from pprint import pprint

# определяем список ключевых слов
KEYWORDS = ['habr', 'raspberry pi', 'web', 'python', 'windows']
MAIN_LINK = 'https://habr.com/ru/all'


# поиск ключевых слов в тексте статьи
def search_key_words_into_article(link_article, keywords):
	headers = Headers(os='win', headers=True).generate()
	ret = requests.get(link_article, headers=headers)
	# ret = requests.get('https://habr.com/ru/post/674810/', headers=headers)
	soup = BeautifulSoup(ret.text, 'html.parser')
	chanks = soup.findAll("p")#.text#.lower()
	text = ""
	for chank in chanks:
		text += chank.text.lower()
	# ищем ключевые слова в тексте
	pattern = ''
	for key in KEYWORDS:
		pattern += r'\b'+key+r'\b|'
	pattern = pattern[:-1] 	# del the last symbol '|'	
	matching = re.findall(pattern, text)
	# определим количество упоминаний каждого ключа в тексте статьи
	return Counter(matching)


headers = Headers(os='win', headers=True).generate()
ret = requests.get(MAIN_LINK, headers=headers)

soup = BeautifulSoup(ret.text, 'html.parser')
articles = soup.findAll("article", {"class": "tm-articles-list__item"})

article_dicts = []
for article in articles:
	# смотрим совпадение по ключевым словам
	hubs = article.findAll("a", {"class": "tm-article-snippet__hubs-item-link"})
	hubs = [hub.span.text.lower() for hub in hubs]
	is_match = False
	matching = [hub for hub in hubs for key in KEYWORDS if key in hub]
	if len(matching):
		is_match = True

	title = article.find("a", {"class": "tm-article-snippet__title-link"})
	ref = 'https://habr.com'+title["href"]
	text_matching = search_key_words_into_article(link_article=ref, keywords=KEYWORDS)
	if text_matching != Counter():
		is_match = True

	if is_match:
		date = article.find("span", {"class":"tm-article-snippet__datetime-published"})
		article_dicts.append({
			"title":title.span.text, 
			"ref":ref,
			"datetime":date.time["datetime"],
			"matching":matching,
			"text_matching":text_matching,
			})


for article in article_dicts:
	if len(article['matching'])>0 or article['text_matching']!=Counter():
		print(f"{article['datetime']} - {article['title']} - {article['ref']}")
		print(f"matched words: {article['matching']}")
		print(f"Text matching:")
		pprint(article['text_matching'])
		print('\n\n')
