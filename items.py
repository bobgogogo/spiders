# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class XiciItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    http_type = scrapy.Field()
    speed = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()

class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
