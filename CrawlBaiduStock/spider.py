'''
通过东方财富网获取股票代码列表
在百度股票构建url获取股票详细信息
'''
import re
import requests
from pyquery import PyQuery as pq

def getHtml(url):
    headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    if r.status_code == 200:
        return r.text
    else:
        return '503'


def getStockList(html):
    doc = pq(html)
    results = doc('#quotesearch ul')
    ulist = []
    count = 0
    for tr in results.items():
        lis = tr('li').text()
        lis = re.findall(r'[(](\d{6})[)]', lis)
        if count==0:
            lis = ['sh'+ i for i in lis]
            sh = lis
        else:
            lis = ['sz'+ i for i in lis]
            sz = lis
        count = count+1
    ulist = sh + sz
    return ulist

def getStockInfo(html):
    doc = pq(html)
    name = doc('.bets-name').text()
    price = doc('._close').text()
    return name, price

if __name__ == "__main__":
    stockList_url = 'http://quote.eastmoney.com/stocklist.html'
    stockInfo_url = 'https://gupiao.baidu.com/stock/'
    list_html = getHtml(stockList_url)
    stockList = getStockList(list_html)
    count = 0
    for i in stockList:
        url = stockInfo_url+str(i)+'.html'
        if getHtml(url) != 503:
            html = getHtml(url)
            name, price= getStockInfo(html)
            p = count*100/len(stockList)
            print('\r'+name+' '+price+'  '+'已完成：{:.2f}%'.format(p))
        else:
            pass
        count = count +1
