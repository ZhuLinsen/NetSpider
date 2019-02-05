import urllib
import urllib.request
import re
#page=urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')

def get_html(url):
    page=urllib.request.urlopen(url)
    html=page.read().decode('utf-8')
    return html

reg=r'src="(.+?\.jpg)"'

imglist=re.findall(reg,get_html('https://tieba.baidu.com/p/5927992534'))
x=0
for img in imglist:
    try:
        urllib.request.urlretrieve(img,'G:\\Pyhton\\NetSpider\\pic2\\%s.jpg' %x)
        x+=1
    except Exception as e:
        print(e)
        print("------------捕获异常----------")
    finally:
        print("下载成功")
        print(img)
    
    
