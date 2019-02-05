'''
通过最好大学网爬取中国top500的大学
'''
import bs4
import lxml

import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
def get_page(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return ''

def get_list_by_pq(html):
    doc = pq(html)
    results = doc('tbody tr')
    ulist = []
    for tr in results.items():
        tds = tr('td').text().split(' ')
        ulist.append([tds[0], tds[1], tds[3]])
    return ulist[:-2]

def printList(ulist):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format('名次', '学校名称', '总分', chr(12288)))
    for i in range(500):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
        with open('Top100.txt', 'a', encoding='gbk') as f:
            f.write(tplt.format(u[0], u[1], u[2], chr(12288))+'\n')
# def get_list_by_bs4(html):
#     soup = BeautifulSoup(html, 'lxml')
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             td = tr('td')
#             print(td[0].string)

if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = get_page(url)
    ulist = get_list_by_pq(html)
    printList(ulist)


