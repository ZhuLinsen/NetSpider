import requests
from pyquery import PyQuery as py

url='https://www.zhihu.com/explore'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    } 
html=requests.get(url,headers=headers).text
doc=py(html)
items=doc('.explore-tab .feed-item').items()
for item in items:
    question=item.find('h2').text()
    author=item.find('.author-link-line').text()
    answer=py(item.find('.content').html()).text()
    with open('ZhihuHotTopic.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join([question, author,answer]))
        f.write('\n'+'='*100+'\n')

    

    