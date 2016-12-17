#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
filename:  search_food.py
function:  search for food top 12 sales
author:  shengdexiang@gmail.com
date:  2016-11-04, Fri
'''

import sys
import os
from bs4 import BeautifulSoup
import re
import argparse
import urllib3
import urllib.request
from collections import OrderedDict

# global settings
search_url = 'http://search.jd.com/Search'
show_food_count = 10
keyword_lists = ('夏威夷果', '松子', '薯片', '旺旺', '好丽友', '饼干',
'蒸蛋糕', '奥利奥', '猪肉铺', '牛肉', '芒果干', '红枣', '枸杞', '巧克力', 
'糖果', '德芙')
Host = 'search.jd.com'
UserAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
AcceptLanguage = 'en-US,en;q=0.5'
AcceptEncoding = 'gzip, deflate'
Connection = 'keep-alive'
UpgradeInsecureRequests = 1
CacheControl = 'max-age=0'

class Searcher:    
    def __init__(self, keyword, cookie):
        self.search_url = search_url + '?keyword=' + urllib.request.quote(keyword) + '&enc=utf-8&psort=3'
        self.headers = {}
        self.headers['Cookie'] = cookie
        #print(self.search_url)
        #print(cookie)

    def set_headers(self):
        self.headers['Host'] = Host
        self.headers['User-Agent'] = UserAgent
        self.headers['Accept'] = Accept
        self.headers['Accpet-Language'] = AcceptLanguage
        self.headers['Accept-Encoding'] = AcceptEncoding
        self.headers['Connection'] = Connection
        self.headers['Upgrade-INsecure-Requests'] = UpgradeInsecureRequests
        self.headers['Cache-Control'] = CacheControl

    def get_html(self, url):
        try:
            http = urllib3.PoolManager()
            response = http.request('GET', url, headers = self.headers)
            if response.status == 200:
                return response.data.decode('utf-8')
            else:
                return None
        except Exception as e:
            print(e.value)
    
    def get_foods_list(self, html_doc):
        try:
            soup = BeautifulSoup(html_doc, 'lxml')
            #print(soup.prettify())
            foods_list = soup.find_all(id = 'J_goodsList')[0].find_all(class_ = 'gl-i-wrap')
            return foods_list[:show_food_count]
        except Exception as e:
            print(e.value)

    def get_food_info(self, foods_list):
        foods_info = []
        for food in foods_list:
            food_info = OrderedDict()
            food_info['title'] = self.get_food_title(food)
            food_info['commits'] = self.get_food_commits_count(food)
            food_info['price'] = self.get_food_price(food)
            food_info['url'] = self.get_food_url(food)
            foods_info.append(food_info)

        return foods_info

    def get_food_title(self, food):
        return food.find_all('div', class_ = 'p-img')[0].a['title']

    def get_food_url(self, food):
        return 'http:' + food.find_all('div', class_ = 'p-img')[0].a['href']

    def get_food_price(self, food):
        return float(food.find_all('div', class_ = 'p-price')[0].i.string)

    def get_food_commits_count(self, food):
        return food.find_all('div', class_ = 'p-commit')[0].a.string

    def go(self):
        self.set_headers()
        html_doc = self.get_html(self.search_url)
        foods_list = self.get_foods_list(html_doc)
        foods_info = self.get_food_info(foods_list)
            
        print('\n按销量排名,找到一下{0}个好吃的:'.format(show_food_count))
        print('*'*50)
        for food_info in foods_info:
            for k, v in food_info.items():
                if k == 'title':
                    print('名称: ', v)
                elif k == 'commits':
                    print('买家: ', v)
                elif k == 'price':
                    print('售价: {0} RMB'.format(v))
                elif k == 'url':
                    print('地址: ', v)
                else:
                    pass
            print('*'*50)

def show_avaiable_keyword_lists():
    for kw in keyword_lists:
        print('-> ' + kw)

def main():
    desc = '''
    Search food top 10(default) sales on [夏威夷果 松子 薯片 旺旺 好丽友 饼干
    蒸蛋糕 奥利奥 猪肉铺 牛肉 芒果干 红枣 枸杞 巧克力 糖果 德芙]
    '''
    parser = argparse.ArgumentParser(prog = sys.argv[0], description = desc)
    parser.add_argument('-k', dest = 'keyword', help = 'Search food given keyword')
    parser.add_argument('-c', dest = 'cookie', help = 'Set cookie')
    args = parser.parse_args()
    if args.keyword == None or args.cookie == None:
        parser.print_usage()
        sys.exit(1)
    if args.keyword not in keyword_lists:
        print('\n输入有误!可选的京东食品种类有：\n')
        show_avaiable_keyword_lists()
        sys.exit(1)

    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        pass
    search = Searcher(args.keyword, args.cookie)
    search.go()

if __name__ == '__main__':
    main()