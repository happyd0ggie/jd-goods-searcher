#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
__filename__:  search_food.py
__function__:  search for food top 12 sales
__author__:  shengdexiang@gmail.com
__date__:  2016-11-04, Fri
'''

try:
    import sys
    import os
    import argparse
    from util import check_modules
    from urllib import request
    from collections import OrderedDict
    import urllib3
    from bs4 import BeautifulSoup
except ImportError:
    check_modules('requirements.txt')
    from bs4 import BeautifulSoup

# global settings
SEARCH_URL = 'http://search.jd.com/Search'
SHOW_FOOD_COUNT = 10
KEYWORD_LIST = ('夏威夷果', '松子', '薯片', '旺旺', '好丽友', '饼干',
                '蒸蛋糕', '奥利奥', '猪肉铺', '牛肉', '芒果干', '红枣',
                '枸杞', '巧克力', '糖果', '德芙')
HOST = 'search.jd.com'
USER_AGENT = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) '
              'Gecko/20100101 Firefox/49.0')
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
ACCEPT_LANGUAGE = 'en-US,en;q=0.5'
ACCEPT_ENCODING = 'gzip, deflate'
CONNECTION = 'keep-alive'
UPGRADE_INSECURE_REQUESTS = 1
CACHE_CTRL = 'max-age=0'

class Searcher:
    """Given a keyword, search top N best saler.

    Given a keyword about some kind of snack, we search the top N best
    salers on JD.
    """
    def __init__(self, keyword, cookie):
        """Initialize keyword and request headers.

        Initialize keyword and cookies(which can be copyed from browser
        by press F12), and request headers that will be sent to
        www.jd.com

        Args:
            keyword: A string represents a kind of snack.
            cookie: A (long) string as cookie used to send request with.

        Returns:
            None.
        """
        self.search_url = '{0}?keyword={1}&enc=utf-8&psort=3'.format(
            SEARCH_URL, urllib.request.quote(keyword))
        self.headers = {}
        self.headers['Cookie'] = cookie

    def set_headers(self):
        """Setting request headers.

        Set headers including host, user-agent, etc.

        Aargs:
            None.

        Returns:
            None.
        """
        self.headers['Host'] = HOST
        self.headers['User-Agent'] = USER_AGENT
        self.headers['Accept'] = ACCEPT
        self.headers['Accpet-Language'] = ACCEPT_LANGUAGE
        self.headers['Accept-Encoding'] = ACCEPT_ENCODING
        self.headers['Connection'] = CONNECTION
        self.headers['Upgrade-INsecure-Requests'] = UPGRADE_INSECURE_REQUESTS
        self.headers['Cache-Control'] = CACHE_CTRL

    def get_html(self, url):
        """Get html page containing information we want.

        This method get html page according given url.

        Args:
            url: A string represents a uri.

        Returns:
            Html page content.
        """
        try:
            http = urllib3.PoolManager()
            response = http.request('GET', url, headers=self.headers)
            if response.status == 200:
                return response.data.decode('utf-8')
            else:
                return None
        except OSError as e:
            print(str(e))

    @staticmethod
    def get_foods_list(html_doc):
        """Get foods list from html.

        Get foods list by parsing html documents with BeautifulSoup
        module.

        Args:
            html_doc: A string represents html documents.

        Returns:
            A list of foods..
        """
        try:
            soup = BeautifulSoup(html_doc, 'lxml')
            #print(soup.prettify())
            foods_list = soup.find_all(id='J_goodsList')[0].find_all(class_='gl-i-wrap')
            return foods_list[:SHOW_FOOD_COUNT]
        except OSError as e:
            print(str(e))

    def get_food_info(self, foods_list):
        """Get food information.

        Get food information, including title, comments, price and uri.

        Args:
            foods_list: A list containing food.

        Returns:
            A list containing formatted food.
        """
        foods_info = []
        for food in foods_list:
            food_info = OrderedDict()  # use OrderedDict instead of Dict
            food_info['title'] = self.get_food_title(food)
            food_info['comments'] = self.get_food_comments_count(food)
            food_info['price'] = self.get_food_price(food)
            food_info['url'] = self.get_food_url(food)
            foods_info.append(food_info)

        return foods_info

    @staticmethod
    def get_food_title(food):
        """Get food name.

        Get food name by parsing xml node.

        Args:
            food: A xml node.

        Returns:
            A string represents food name.
        """
        return food.find_all('div', class_='p-img')[0].a['title']

    @staticmethod
    def get_food_url(food):
        """Get food uri.

        Get food uri by parsing xml node.

        Args:
            food: A xml node.

        Returns:
            A string represents food uri.
        """
        return 'http:' + food.find_all('div', class_='p-img')[0].a['href']

    @staticmethod
    def get_food_price(food):
        """Get food price.

        Get food price by parsing xml node.

        Args:
            food: A xml node.

        Returns:
            A string represents food price.
        """
        return float(food.find_all('div', class_='p-price')[0].i.string)

    @staticmethod
    def get_food_comments_count(food):
        """Get food comment count..

        Get food comment count by parsing xml node.

        Args:
            food: A xml node.

        Returns:
            A string represents food comment count.
        """
        return food.find_all('div', class_='p-commit')[0].a.string

    def go(self):
        self.set_headers()
        html_doc = self.get_html(self.search_url)
        foods_list = self.get_foods_list(html_doc)
        foods_info = self.get_food_info(foods_list)

        print('\n按销量排名,找到一下{0}个好吃的:'.format(SHOW_FOOD_COUNT))
        print('*' * 50)
        for food_info in foods_info:
            for k, v in food_info.items():
                if k == 'title':
                    print('名称: ', v)
                elif k == 'comments':
                    print('买家: ', v)
                elif k == 'price':
                    print('售价: {0} RMB'.format(v))
                elif k == 'url':
                    print('地址: ', v)
                else:
                    pass
            print('*'*50)

# get only a few foods
def show_avaiable_keyword_lists():
    """Show avaiable keywords we support.

    Show avaiable keywords this script support, as for now we only
    support a few.

    Args:
        None.

    Returns:
        None.
    """
    for kw in KEYWORD_LIST:
        print('-> ' + kw)

def get_argparser():
    """Get a argument parser.
    
    This method makes a argument parser.

    Args:
        None.

    Returns:
        None
    """
    desc = '''
    Search food top 10(default) sales on [夏威夷果 松子 薯片 旺旺 好丽友 饼干
    蒸蛋糕 奥利奥 猪肉铺 牛肉 芒果干 红枣 枸杞 巧克力 糖果 德芙]
    '''
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=desc)
    parser.add_argument('-k', dest='keyword', help='Search food given keyword')
    parser.add_argument('-c', dest='cookie', help='Set cookie')

    return parser

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        pass

def main():
    parser = get_argparser()
    args = parser.parse_args()

    if not args.keyword or not args.cookie:
        parser.print_usage()
        sys.exit(1)
    if args.keyword not in KEYWORD_LIST:
        print('\n输入有误!可选的京东食品种类有：\n')
        show_avaiable_keyword_lists()
        sys.exit(1)

    clear_screen()

    search = Searcher(args.keyword, args.cookie)
    search.go()

if __name__ == '__main__':
    main()
