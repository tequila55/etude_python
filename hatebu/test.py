# -*- coding: utf-8 -*-

import pandas
import json
import sys
from bs4 import BeautifulSoup as bs
from urllib import request

def scraping():
    #url
    #url = "http://www.yomiuri.co.jp/"
    url = "https://b.hatena.ne.jp/Apeman/"
    #url = "https://b.hatena.ne.jp/apesnotmonkeys/"

    #get html
    html = request.urlopen(url)

    print(vars(html))

    #set BueatifulSoup
    soup = bs(html, "html.parser")

    #print(soup) 
    
    '''
    #get headlines
    mainNewsIndex = soup.find("ul", attrs={"class", "list-main-news"})
    headlines = mainNewsIndex.find_all("span", attrs={"class", "headline"})

    #print headlines
    for headline in headlines:
        print(headline.contents[0], headline.span.string)
    '''

    return

if __name__ == '__main__':
#    if len(sys.argv) != 3:
#       print('ERROR: Input file and output file required.')
#        print('USAGE: ' + sys.argv[0] + ' <in_file> <out_file>')
#        print('       in_file:  it must be one json per line.')
#        print('       out_file: .csv or anything (e.g. .txt)')
#        exit()

    scraping()

