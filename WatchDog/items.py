# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):

    link = scrapy.Field()
    product_type = scrapy.Field()
    img_url = scrapy.Field()
    is_available = scrapy.Field()
