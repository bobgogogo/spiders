# -*- coding: utf-8 -*-
from spider.sqldb import Db
import json
import codecs
import requests

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiciPipeline(object):
    def __init__(self):
        self.file = codecs.open('questions.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):

        # return item
        db = Db()
        res = db.insert('ip_proxy_pool',item)
        lines = json.dumps(res, ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def close_spider(self, spider):
        self.file.close()

