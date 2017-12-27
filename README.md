# jd-goods-searcher
jd-goods-searcher is a searcher to Search top N best sales foods.

## How to use
### Prerequisites
* Install Python3 on your system. Refer to **[Install Python3](https://docs.python.org/3/using/index.html)**
* Install BeautifulSoup module.
```
$ pip3 install bs4
```
* Install lxml module.
```
$ pip3 install lxml
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
### Example
```
sdx@sdx-pc:~/Documents/code/python/jd-goods-searcher$ python3 search_food.py -c "__jda=122270672.953723416.1481940540.1481940540.1481953894.1; __jdb=122270672.1.953723416|1.1481953894; __jdc=122270672; __jdv=122270672|direct|-|none|-|1481953893940; o2-webp=true; __jdu=953723416" -k 夏威夷果



按销量排名,找到一下10个好吃的:
**************************************************
名称:  三只松鼠零食特产干果年货礼盒 碧根果 夏威夷果 坚果大礼包火红A 1493g
买家:  2.5万+
售价: 128.0 RMB
地址:  http://item.jd.com/3995878.html
**************************************************
名称:  【三只松鼠_坚果组合750g】夏威夷果碧根果手剥巴旦木紫薯花生共4袋
买家:  8.8万+
售价: 75.9 RMB
地址:  http://item.jd.com/1206033312.html
**************************************************
名称:  【京东超市】三只松鼠 坚果炒货 零食奶油味 夏威夷果265g/袋
买家:  24万+
售价: 25.9 RMB
地址:  http://item.jd.com/2518087.html
**************************************************
名称:  新货【三只松鼠_夏威夷果265gx2袋】零食坚果炒货干果奶油味送开口器
买家:  25万+
售价: 48.9 RMB
地址:  http://item.jd.com/1018421638.html
**************************************************
名称:  满减【三只松鼠_夏威夷果185g】零食坚果特产炒货干果奶油味送开口器
买家:  10万+
售价: 33.8 RMB
地址:  http://item.jd.com/1047051827.html
**************************************************
名称:  新货【百草味】夏威夷果200gx3袋 坚果炒货零食干果 奶油味 包装内含开果器
买家:  16万+
售价: 46.9 RMB
地址:  http://item.jd.com/1003395585.html
**************************************************
名称:  【三只松鼠_坚果组合630g】零食夏威夷果碧根果手剥巴旦木共3袋
买家:  5.9万+
售价: 65.9 RMB
地址:  http://item.jd.com/1123745314.html
**************************************************
名称:  【京东超市】良品铺子夏威夷果280g*2 奶油味 坚果炒货干果 休闲零食
买家:  5.8万+
售价: 36.9 RMB
地址:  http://item.jd.com/1012138835.html
**************************************************
名称:  三只松鼠零食特产干果年货礼盒 碧根果 夏威夷果 坚果大礼包火红B 1765g
买家:  2.5万+
售价: 168.0 RMB
地址:  http://item.jd.com/3987510.html
**************************************************
名称:  【京东超市】百草味 年货坚果零食干果 夏威夷果奶油味200g/袋 内含开果器
买家:  20万+
售价: 17.9 RMB
地址:  http://item.jd.com/1150551.html
**************************************************
```
That's it.
### Note
Cookie can be copied from browser by press f12 after you open https://www.jd.com
