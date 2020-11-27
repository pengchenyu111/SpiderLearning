# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 可以在这里写多个Pipeline，注意再settings中使用即可

import logging
import csv

logger = logging.getLogger(__name__)


class MyspiderPipeline:
    # spider参数可以判断是哪个爬虫传递过来的item
    def process_item(self, item, spider):
        # 要在settings中开启pipeline
        if spider.name == "maoyanmoviestop100":
            logger.info(item)
            save_maoyan_movie_top100(item)
        return item


def save_maoyan_movie_top100(item):
    filename = 'maoyan_movie_top100.csv'
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['rank', 'movie_id', 'name', 'actors', 'time', 'score', 'poster_url', 'film_url']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(item)
