# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
import logging
from yangguang.items import YangguangItem

logger = logging.getLogger(__name__)


class YangguangPipeline:
    def process_item(self, item, spider):
        if isinstance(item, YangguangItem):
            logger.info(item)
            save_maoyan_movie_top100(item)
        return item

    def open_spider(self, spider):
        # 在爬虫开启时执行一次
        # 一般这里用来方数据库连接开启，或文件开启
        pass

    def close_spider(self, spider):
        # 在爬虫关闭时执行一次
        # 一般这里用来方数据库连接关闭，或文件关闭
        # 注意要是文件操作的话，python是在关闭后菜写入数据的，所以若是之前出错了，可能导致前面的数据也写不进去
        pass

def save_maoyan_movie_top100(item):
    filename = 'questions.csv'
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'status', 'title', 'href', 'response_time', 'publish_time', 'content_text', 'content_img']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(item)
