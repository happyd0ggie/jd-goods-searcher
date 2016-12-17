# jd-goods-searcher
jd-goods-searcher is a searcher to Search top N best sales foods.

## How to use
### Prerequisites
* Install Python3 on your system. Refer to **[Install Python3](https://docs.python.org/3/using/index.html)**
* Install BeautifulSoup module.
```
$ pip3 install bs4
```
### Usage(command line only)
```
$ python3 search_food.py --help
usage: search_food.py [-h] [-k KEYWORD] [-c COOKIE]

Search food top 10(default) sales on [夏威夷果 松子 薯片 旺旺 好丽友 饼干 蒸蛋糕 奥利奥 猪肉铺 牛肉 芒果干
红枣 枸杞 巧克力 糖果 德芙]

optional arguments:
  -h, --help  show this help message and exit
  -k KEYWORD  Search food given keyword
  -c COOKIE   Set cookie
```
That's it.
### Note
Cookie can be copy from browser by press f12 after you open https://www.jd.com