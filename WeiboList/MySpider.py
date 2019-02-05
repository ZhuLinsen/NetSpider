import requests
from pymongo import MongoClient

client=MongoClient()
db=client['weibo']
collection=db['mytest']

base_url='https://m.weibo.cn/api/container/getIndex?containerid=2304132895532901_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page=2'

def get_page(url):
    response=request.get(url)
    
    