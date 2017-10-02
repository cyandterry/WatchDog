import os
import scrapy

from scrapy import Selector
from WatchDog.constants import BASE_URL
from WatchDog.items import Product


class SupremeSpider(scrapy.Spider):
    name = 'supremespider'
    start_urls = ['http://www.supremenewyork.com/shop/all']

    def parse(self, response):
        sel = Selector(text=response.body, type="html")
        articles = sel.xpath('//article')
        available_list = []
        all_list = []

        for a in articles:
            url = str(a.css('a').xpath('@href').extract_first())
            link = BASE_URL + url

            url_el = url.split('/')
            product_type = url_el[2]
            product = url_el[-2]
            alt = url_el[-1]

            img_url = str(a.css('img')[0].xpath('@src').extract_first())
            is_available = not ('sold_out_tag' in a.extract())

            yield Product(
                product=product,
                alt=alt,
                link=link,
                product_type=product_type,
                img_url='http:' + img_url,
                is_available=is_available,
            )
