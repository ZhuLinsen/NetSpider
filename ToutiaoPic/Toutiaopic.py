import requests
import os
from urllib.parse import urlencode 
from hashlib import md5
from multiprocessing.pool import Pool
from requests import codes

#构建函数获取源代码
def get_page(offset):
    params={
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
        }
    url='https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url)
        if response.status_code==200:
            #print(response.content)
            return response.json()
    except requests.ConnectionError:
        return None 

    
#获取图片的标题和图片链接
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('cell_type') is not None:
                continue
            title=item.get('title')
            images=item.get('image_list')
            for image in images:
                yield{
                    'image':'https:'+image.get('url'),
                    'title':title
                    }
  

       
def save_image(item):
    
    try:
        response=requests.get(item.get('image'))
        if response.status_code==200:
            file_path='images'+os.path.sep+'{0}.{1}'.format(md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download',file_path)
    except requests.ConnectionError:
        print('Fail to save images')


       
def main(offset):
    json=get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START=0
GROUP_END=7

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
   


