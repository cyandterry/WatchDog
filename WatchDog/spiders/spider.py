import os
import scrapy
import webbrowser

from scrapy import Selector
from WatchDog.items import Product

class SupremeSpider(scrapy.Spider):
    name = 'supremespider'
    start_urls = ['http://www.supremenewyork.com/shop/all']
    BASE_URL = 'http://www.supremenewyork.com'
    CHECK_ALL = True

    def parse(self, response):
        sel = Selector(text=response.body, type="html")
        articles = sel.xpath('//article')
        available_list = []
        all_list = []

        for a in articles:
            link = str(a.css('a').xpath('@href').extract_first())
            product_type = str(link.split('/')[2])
            img_url = str(a.css('img')[0].xpath('@src').extract_first())
            is_available = not ('sold_out_tag' in a.extract())
            p = Product(
                link=self.BASE_URL + link,
                product_type=product_type,
                img_url='http:' + img_url,
                is_available=is_available,
            )
            if is_available:
                available_list.append(p)
            all_list.append(p)

        self.check_products(available_list)

    def check_products(self, p_list):
        rows = ''
        for p in p_list:
            if self.CHECK_ALL or p['product_type'] in TOP_PRIORITY_PRODUCTS:
                img = '<img src="%s">' % p['img_url']
                link = '<a href="%s" target="_blank">Click to Buy</a>' % p['link']
                rows += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (
                    img,
                    p['product_type'],
                    link,
                )

        file_name = 'product.html'
        f = open(file_name,'w')

        message = """
<html>
<head></head>
<body>
  %s
</body>
</html>
"""

        table = """
<table>
    <tr>
       <th>Img</th>
       <th>Type</th>
       <th>URL</th>
    </tr>
    %s
</table>
""" % rows
        f.write(message % table)
        f.close()
        webbrowser.open('file://' +  os.getcwd() + '/' + file_name)


class ProductType:
    BAG = 'bags'
    TOP_SWEATERS = 'tops-sweaters'
    SHOE = 'shoes'
    SWEATSHIRT = 'sweatshirts'
    HAT = 'hats'
    ACCESSORY = 'accessories'
    SKATE = 'skate'
    SHIRT = 'shirts'
    JACKET = 'jackets'
    T_SHIRT = 't-shirts'
    PANTS = 'pants'


TOP_PRIORITY_PRODUCTS = [
    ProductType.BAG,
    ProductType.SWEATSHIRT,
    ProductType.T_SHIRT,
    ProductType.TOP_SWEATERS,
]
