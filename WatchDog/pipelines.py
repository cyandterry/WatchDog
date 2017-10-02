import csv
import os
import webbrowser

from scrapy.exporters import CsvItemExporter

from WatchDog.constants import InventoryActivityType
from WatchDog.items import InventoryActivity


class CompareProductPipeline(object):

    def __init__(self):
        self.inventory = {}
        with open('product.csv') as product_csv:
            input_file = csv.DictReader(product_csv)
            for row in input_file:
                inventory_key = row['product'] + '_' + row['alt']
                self.inventory[inventory_key] = row

        self.file = open('inventory_actvity.csv', 'a')
        self.writer =  csv.writer(self.file)


    def process_item(self, item, spider):
        inventory_key = item['product'] + '_' + item['alt']
        if inventory_key not in self.inventory:
            new_activity = InventoryActivity(
                item=item,
                activity_type=InventoryActivityType.NEW_ITEM,
            )
            self.writer.writerow(new_activity.to_csv_row())
        else:
            inventory_item = self.inventory[inventory_key]
            if str(item['is_available']) != inventory_item['is_available']:
                new_activity = InventoryActivity(
                    item=item,
                    activity_type=InventoryActivityType.AVAILABILITY_CHANGE,
                    old_item=inventory_item,
                )
                self.writer.writerow(new_activity.to_csv_row())

        return item

    def close_spider(self, spider):
        self.file.close()


class NewProductPipeline(object):

    def __init__(self):
        self.file = open('product.csv', 'w')
        self.exporter = CsvItemExporter(self.file, unicode)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class DisplayPipeline(object):

    def __init__(self):
        self.file = open('product.html', 'w')
        self.rows = ''

    def process_item(self, item, spider):
        if not item['is_available']:
            return item

        img = '<img src="%s">' % item['img_url']
        link = '<a href="%s" target="_blank">Click to Buy</a>' % item['link']
        self.rows += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (
            img,
            item['product_type'],
            link,
        )
        return item

    def close_spider(self, spider):
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
""" % self.rows
        self.file.write(message % table)
        self.file.close()
        webbrowser.open('file://' +  os.getcwd() + '/product.html')
