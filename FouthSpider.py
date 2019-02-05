import re
import requests
s=''' </li><li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30327026/?icn=index-latestbook-subject" title="杨天乐买房记">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29870594.jpg" class=""
                  width="115px" height="172px" alt="杨天乐买房记">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30327026/?icn=index-latestbook-subject"
                  title="杨天乐买房记">杨天乐买房记</a>
              </div>
              <div class="author">
                杨时旸
              </div>
              <div class="more-meta">
                <h4 class="title">
                  杨天乐买房记
                </h4>
                <p>
                  <span class="author">
                    杨时旸
                  </span>
                  /
                  <span class="year">
                    2018-10-1
                  </span>
                  /
                  <span class="publisher">
                    四川文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  
                </p>
              </div>
            </div>
          </li>'''
result=re.findall('<li.*?cover.*?href="(.*?)".*?title="(.*?)">.*?=author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',s,re.S)
print(result)