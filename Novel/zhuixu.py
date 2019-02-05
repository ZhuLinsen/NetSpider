from bs4 import BeautifulSoup
from multiprocessing import Pool
from pyquery import PyQuery as pq
import requests,time

#获得单章的内容
def get_html(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    r = requests.get(url,headers=header)
    r.encoding='gbk'
    html = r.text  
    soup = BeautifulSoup(html,'lxml')
    title = soup.h1.string
    article = soup.select('.content_read .box_con #content')
    article = article[0].get_text()
    return title,article.split()

#存储模块
def save_txt(title,text):
    with open('zhuixu.txt','a',encoding='utf-8') as f:
        f.write(title+'\n'+'-'*50+'\n')
        print('正在写入 '+title)
        for i in text:
            f.write('    '+i+'\n'*2)
            
#获得全部章节链接            
def get_url(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    r = requests.get(url, headers = header).text
    doc = pq(r)
    a = doc('dd a')
    list = []
    for i in a.items():
        list.append(i.attr('href'))
    return list[8:]
                 
def main(url):    
    text =get_html(url)          
    save_txt(text[0],text[1])    

#章节目录链接 
if __name__=='__main__':
    url='https://www.booktxt.net/2_2220/'
    lis = get_url(url)
    p=Pool()
    start = time.time()
    for i in lis:
        p.map(main,(url+i,))
    end = time.time()
    print('下载完成，用时一共是%s' %(end-start))
    
