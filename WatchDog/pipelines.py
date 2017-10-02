import os
import webbrowser

from scrapy.exporters import CsvItemExporter


class CSVPipeline(object):

    def __init__(self):
        self.file = open('product.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, unicode)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class HMTLPipeline(object):

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
