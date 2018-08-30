# -*- coding: utf-8 -*-
from spider.sqldb import Db
import json
import codecs
import requests
import time

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class XiciPipeline(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
    }
    url = 'http://www.baidu.com/'


    def process_item(self, item, spider):
        db = Db()
        proxies = {(item['http_type'].lower()):item['http_type'].lower()+'://'+item['ip']+':'+item['port']}
        s = requests.session()
        s.keep_alive = False
        try:
            page = requests.get(self.url, proxies=proxies,headers=self.headers,timeout=2)
            print(page.status_code)
            if page.status_code==200:
                item['create_time'] = time.time()
                res = db.insert('ip_proxy_pool',item)
        except requests.exceptions.Timeout as e:
            print('<===========requestError==========>timeout============>','status_code'+page.status_code,str(e))
        except Exception as a:
            print('------------Error---------->erroe------------>',str(a))
        return item

    def close_spider(self, spider):
        pass

