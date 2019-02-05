#          爬取豆瓣读书首页数据
import re
import requests

content=requests.get('https://book.douban.com/').text
print(content)
#pattern=re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
results=re.search('<li.*?cover.*?href="(.*?)".*?title="(.*?)">',content,re.S)
print(results)