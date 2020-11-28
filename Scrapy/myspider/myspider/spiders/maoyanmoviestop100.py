import scrapy
import re
import logging
from myspider.items import MaoyanMoviesItem

logger = logging.getLogger(__name__)

BASE_URL = "https://maoyan.com"


class Maoyanmoviestop100Spider(scrapy.Spider):
    name = 'maoyanmoviestop100'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def parse(self, response):
        movie_list = response.xpath("//dl//dd")
        for movie in movie_list:
            item = MaoyanMoviesItem()
            item['rank'] = movie.xpath('./i/text()').get()
            item['movie_id'] = re.findall('{movieId:(\d+)}', movie.xpath('a/@data-val').get())[0]
            item['name'] = movie.xpath('./a/@title').get()
            item['actors'] = re.findall('主演：(.*)', movie.xpath('./div/div/div/p[@class="star"]/text()').get().strip())[0]
            item['time'] = re.findall('上映时间：(.*)', movie.xpath('./div/div/div/p[@class="releasetime"]/text()').get().strip())[0]
            item['score'] = movie.xpath("./div/div/div[2]/p/i[1]/text()").get() + movie.xpath("./div/div/div[2]/p/i[2]/text()").get()
            item['poster_url'] = movie.xpath("./a/img[2]/@data-src").get()
            item['film_url'] = BASE_URL + movie.xpath("./a/@href").get()
            yield item
        # 下一页的地址
        next_url = response.xpath('//ul[@class="list-pager"]/li[last()]/a/@href').get()
        if next_url is not None:
            next_url = 'https://maoyan.com/board/4' + next_url
            logger.info(next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
