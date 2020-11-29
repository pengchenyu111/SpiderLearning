# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from my_movie_crawlspider.items import MaoyanMoviesItem
import pymysql


class MyMovieCrawlspiderPipeline:

    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=spider.settings['MYSQL_HOST'],
            user=spider.settings['MYSQL_USERNAME'],
            password=spider.settings['MYSQL_PASSWORD'],
            db=spider.settings['MYSQL_DB'],
            charset=spider.settings['MYSQL_DB_CHARSET']
        )

    def process_item(self, item, spider):
        if isinstance(item, MaoyanMoviesItem):
            try:
                self.save_movie_meta(item)
            except Exception as e:
                print(e)

    def close_spider(self, spider):
        self.connection.close()

    def save_movie_meta(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO my_movie (%s) VALUES (%s)' % (fields, temp)
        self.connection.cursor().execute(sql, tuple(i.strip() for i in values))
        return self.connection.commit()
