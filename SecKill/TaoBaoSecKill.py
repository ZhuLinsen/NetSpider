import os 
import time
from selenium import webdriver
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
try:
    button=browser.find_element_by_class_name('btn-login')
    button.click()
    wait=WebDriverWait(browser,10)
    login=wait.until(EC.presence_of_all_elements_located((By.ID,'J_Quick2Static')) )
    login[0].click()
    time.sleep(1)
    
    
except Exception as e:
    time.sleep(0.5)
    print(e)
print('下一步')
    
    