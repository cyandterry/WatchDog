import scrapy
import time
import datetime

from WatchDog.constants import InventoryActivityType

class Product(scrapy.Item):

    product = scrapy.Field()
    alt = scrapy.Field()
    link = scrapy.Field()
    product_type = scrapy.Field()
    img_url = scrapy.Field()
    is_available = scrapy.Field()


class InventoryActivity:

    def __init__(self, item, activity_type, old_item=None):
        self.item = item
        self.activity_type = activity_type
        self.old_item = old_item
        self.ts = int(time.time())

    def __str__(self):
        if self.activity_type == InventoryActivityType.NEW_ITEM:
            return 'New Item Loaded'
        elif self.activity_type == InventoryActivityType.AVAILABILITY_CHANGE:
            return 'Item availability changed from %s to %s' % (
                self.old_item['is_available'],
                self.item['is_available'],
            )

    def to_csv_row(self):
        time_str =  datetime.datetime.fromtimestamp(
            self.ts
        ).strftime('%Y-%m-%d %H:%M')
        return [
            time_str,
            str(self),
            self.activity_type,
            self.item['link'],
        ]
