# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from time import sleep

user = 'Apeman'
url = 'http://b.hatena.ne.jp/' + user + '/bookmark'

r = requests.get(url)
page = 1

while True:
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup)

    #　ブックマークを取得するコードを書く

    # 「次のページ」がなくなると最終ページということを使用
    if soup.find_all(class_="centerarticle-pager-next"):
        page += 1
        r = requests.get(url + '?page=' + str(page))
    else:
        break
    sleep(10)

