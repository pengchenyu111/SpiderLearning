# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 可以在这里写多个Pipeline，注意再settings中使用即可

class MyspiderPipeline:
    # spider参数可以判断是哪个爬虫传递过来的item
    def process_item(self, item, spider):
        # 要在settings中开启pipeline
        print(item)
        return item
