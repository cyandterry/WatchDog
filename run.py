#!/usr/bin/env python

import scrapy
from scrapy.crawler import CrawlerProcess

from WatchDog.spiders.spider import SupremeSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SupremeSpider)
process.start()
