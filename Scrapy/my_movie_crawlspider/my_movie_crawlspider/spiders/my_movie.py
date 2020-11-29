import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import re
from my_movie_crawlspider.items import MaoyanMoviesItem


class MyMovieSpider(CrawlSpider):
    name = 'my_movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    rules = (
        Rule(LinkExtractor(allow=r'/films/\d+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'\?offset=\d+'), follow=True),
    )

    def parse_item(self, response):
        item = MaoyanMoviesItem()
        item['movie_id'] = re.findall('{movieid:(\d+)}', response.xpath('//div[@class="action clearfix"]/@data-val').get())[0]
        item['name'] = response.xpath('//h1[@class="name"]/text()').get()
        item['time'] = response.xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()').get()
        item['score'] = response.xpath('//div[@class="movie-index-content score normal-score"]/span/span/text()').get()
        item['poster_url'] = response.xpath('//div[@class="avatar-shadow"]/img/@src').get()
        yield item
    # 这里也可以再去写深一层的详情页，和之前一样
