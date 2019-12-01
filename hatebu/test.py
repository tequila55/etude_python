# -*- coding: utf-8 -*-

from pathlib import Path
import pandas
import json
import sys
from bs4 import BeautifulSoup as bs
from urllib import request

folder='monkey'
name='*.html'

def analyze(html):
    soup = bs(html, 'lxml')
    a = soup.find_all(class_='centerarticle-entry-title')
    for t in a:
        print(t.text)
        '''
        print('-'*30)
        b = t.find(class_='centerarticle-entry-summary')
        if(b):
            print(b.text)
        print('='*30)
        '''

def scraping():
    p=Path(folder)
    for f in p.glob(name):
        #print(f)
        with open(f,'r',encoding='utf_8_sig') as fin:
            html=fin.read()
            analyze(html)
            # for test uncomment this return
            #return
    
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

