# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from den_crawler.items import DenCrawlerItem
import codecs


class DenSpider(CrawlSpider):
    name = 'den'
    cnt=1
    allowed_domains = ['www.donya-e-eqtesad.com', 'donya-e-eqtesad.com']
    start_urls = []
    start_id = 4240 # 1396/10/23
    end_id = 4803 # 1398/10/23
    url_format = 'https://donya-e-eqtesad.com/%D8%B1%D9%88%D8%B2%D9%86%D8%A7%D9%85%D9%87-%D8%B4%D9%85%D8%A7%D8%B1%D9%87-'
    for id in range(start_id,end_id+1) :
        start_urls.append(f'{url_format}{id}/')
    rules = [Rule(LinkExtractor(allow=r'/[^/]+\d+/\d+[^/]+$',), callback='parse_news', follow=False),]

    def parse_news(self, response):
        try :
            self.logger.info(f'##### ---> #### {self.cnt}')
            
            # self.logger.info(f"\n parse_news called\n{response.request.url}\n")
            item = DenCrawlerItem()
            item['tags'] = "^".join(response.xpath('//div[@class="article-tag"]/a/@title').getall())
            item['serial_id'] = response.xpath("//a[starts-with(@href, '/fa/tiny')]/@href").get().split('-')[1]
            item['news_id'] = response.url.split("/")[4].split("-")[0]
            item['news_date'] = response.xpath('//time/@datetime').get()
            self.logger.info(f"Tags : {item['tags']}")
            self.write_news_info(item)
            self.cnt +=1
        except :
            pass
        
    def write_news_info(self, item):
        f = codecs.open('news_tags.csv', "a", encoding="utf8")
        row_csv = "{0},{1},{2},{3}\r\n".format(item["serial_id"],
                                                    item["news_date"],
                                                    item["news_id"],
                                                    item["tags"])
        f.write(row_csv)
        f.close()
        

# response.xpath('//time/@datetime').get()
# response.xpath("//a[starts-with(@href, '/fa/tiny')]/@href").get().split('-')[1]
# request.url.split("/")[4].split("-")[0]
# "^".join(response.xpath('//div[@class="article-tag"]/a/@title').getall())