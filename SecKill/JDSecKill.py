# 仅用于试验京东秒杀专栏

import os 
import time
from selenium import webdriver
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d9qTFmpH&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F')
try:
    #wait=WebDriverWait(browser,10)
    #login=wait.until(EC.presence_of_all_elements_located((By.ID,'J_Quick2Static')) )
    login=browser.find_element_by_id('J_Quick2Static')
    login.click()
    time.sleep(1)
    
    
except Exception as e:
    time.sleep(0.5)
    print(e)
print('下一步')