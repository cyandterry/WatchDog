#!/usr/bin/env python

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from WatchDog.spiders.spider import SupremeSpider

process = CrawlerProcess(get_project_settings())

process.crawl(SupremeSpider)
process.start()
