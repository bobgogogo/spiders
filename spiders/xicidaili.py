# -*- coding: utf-8 -*-
import scrapy
import time
from spider.items import XiciItem
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/']
    header = {'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTRmZTkxNGU0MTE3NWEzYjYwN2E1ZTAzMDQ2NGUxMDljBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMW5NMkxreUkvalFySUdnYmFFSFlsWDYvRklSa0t0NEgzc29scG5PbHlkNnM9BjsARg%3D%3D--7359170b7e011adba6aff309d01b6b814cf8cdb1; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1534836306,1534843089; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1534908158',
              'Host':'www.xicidaili.com','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    def start_requests(self):
        for i in range(1,2):
            yield scrapy.Request(url=self.start_urls[0]+str(i),headers=self.header,callback=self.parse)

    def parse(self, response):
        items = []
        lists = response.xpath("//table[@id='ip_list']/tr[@*]")

        for li in lists:
            item = XiciItem()
            item['ip'] = li.xpath("./td[2]/text()").extract_first()
            item['port'] = li.xpath("./td[3]/text()").extract_first()
            item['http_type'] = li.xpath("./td[6]/text()").extract_first()
            item['speed'] = (li.xpath('./td[7]/div/@title').extract_first())[0:-1]
            item['create_time'] = time.time()
            items.append(item)

        return items
        # filename = response.url.split("/")[2]
        # with open(filename, 'wb') as f:
        #     print(1)



if __name__=='__main__':
    for i in range(1,4):
        print(i)