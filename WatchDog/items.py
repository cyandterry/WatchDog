import scrapy


class Product(scrapy.Item):

    product = scrapy.Field()
    alt = scrapy.Field()
    link = scrapy.Field()
    product_type = scrapy.Field()
    img_url = scrapy.Field()
    is_available = scrapy.Field()
