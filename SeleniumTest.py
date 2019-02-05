from selenium import webdriver
import time

browser=webdriver.Chrome()
url='https://www.zhihu.com/explore'
browser.get(url)

browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.qq.com')
browser.back()
time.sleep(1)
browser.forward()
browser.close()