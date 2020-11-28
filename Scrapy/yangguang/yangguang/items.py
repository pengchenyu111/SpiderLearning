# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    id = scrapy.Field()
    status = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    response_time = scrapy.Field()
    publish_time = scrapy.Field()
    content_text = scrapy.Field()
    content_img = scrapy.Field()
