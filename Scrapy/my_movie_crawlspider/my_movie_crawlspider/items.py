# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyMovieCrawlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MaoyanMoviesItem(scrapy.Item):
    movie_id = scrapy.Field()
    name = scrapy.Field()
    time = scrapy.Field()
    score = scrapy.Field()
    poster_url = scrapy.Field()
