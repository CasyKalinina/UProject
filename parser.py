# -*- coding: utf-8 -*-
import requests
import json
import datetime
import io
from bs4 import BeautifulSoup

page_url = 'https://vc.ru'
path = "articles.json"

def get_html_page(page_url):
    return requests.get(page_url)


def find_articles(html_page):

    soup = BeautifulSoup(html_page, 'html.parser')
    articles = []

    for article in soup.find_all('h2'):
        text = article.text.strip()
        articles.append(text)
    return articles


def publish_report(path, articles):
    result = {"url": page_url,
              "creationDate": datetime.datetime.now().strftime("%b %m, %Y, %H:%M"),
              "articles": articles}


    with io.open(path, 'w', encoding='utf8') as json_file:
        json.dump(result, json_file, ensure_ascii=False)


html_page = get_html_page(page_url)
articles = find_articles(html_page.text)
publish_report(path, articles)
