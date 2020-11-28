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


def save_maoyan_movie_top100(item):
    filename = 'questions.csv'
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'status', 'title', 'href', 'response_time', 'publish_time', 'content_text', 'content_img']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(item)
