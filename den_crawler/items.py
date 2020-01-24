# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DenCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    serial_id = scrapy.Field()
    news_id = scrapy.Field()
    news_date = scrapy.Field()
    tags= scrapy.Field()
