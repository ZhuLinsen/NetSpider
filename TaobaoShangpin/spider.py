from selenium import webdriver
from urllib.parse import quote


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

KEYWORD = 'ipad'

def get_index():
    try:
        url='https://s.taobao.com/search?q='+quote(KEYWORD)
        response=browser.get(url)
        print(response)
    
    except Exception as e:
        print(e)

get_index()