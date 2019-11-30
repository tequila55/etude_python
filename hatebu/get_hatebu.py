# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from time import sleep

# target config
user = 'apesnotmonkeys'
url = 'http://b.hatena.ne.jp/' + user + '/bookmark'
page = 1

# output file
prefix='apesnotmonkeys/apes_'
suffix='.html'

while True:
    r = requests.get(url + '?page=' + str(page))
    #soup = BeautifulSoup(r.text, 'html.parser')
    soup = BeautifulSoup(r.text, 'lxml')
    #print(soup)

    out_file = prefix + str(page).zfill(5) + suffix
    with open (out_file,'w',encoding='utf_8_sig') as fout:
        fout.write(r.text)
    
    print(out_file)

    if soup.find_all(class_="centerarticle-pager-next"):
        page += 1
    else:
        break
    #sleep(1)

