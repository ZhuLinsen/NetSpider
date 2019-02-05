import requests
import re
import time
import json
from multiprocessing import Pool
from requests.exceptions import RequestException
from nltk.parse.bllip import _ensure_ascii

def get_one_html(url):
    try:
        header={'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
         }
        html=requests.get(url,headers=header)
        if html.status_code == 200:
            return html.text
        return None
    except RequestException:
        return None

def get_result(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?<img data-src="(.*?)".*?'
                        +'class="name"><a.*?title="(.*?)".*?<p class="star">(.*?)'
                        +'</p>.*?class="releasetime">(.*?)</p>.*?</dd>',re.S)
    result=re.findall(pattern,html)
    for item in result:
        yield{
            'index':item[0],
            'img':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4][5:]
            }

def get_url_onebyone(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_html(url)
    res = get_result(html)
    for item in res:
        writer_into_txt(item)
        print(item)

def writer_into_txt(content):
    with open('top100.txt','a' ) as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
if __name__ =='__main__':        
    for m in range(10):
        #pool=Pool()
        #pool.map(get_url_onebyone,[i*10 for i in range(10)])
        get_url_onebyone(m*10)
        time.sleep(1)



