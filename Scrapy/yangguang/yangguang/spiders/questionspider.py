import scrapy
import re
from yangguang.items import YangguangItem

BASE_URL = 'http://wz.sun0769.com'


class QuestionspiderSpider(scrapy.Spider):
    name = 'questionspider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    def parse(self, response):
        li_list = response.xpath('//li[@class="clear"]')
        for li in li_list:
            item = YangguangItem()
            item['id'] = li.xpath('./span[@class="state1"]/text()').get()
            item['status'] = li.xpath('./span[@class="state2"]/text()').get().strip()
            item['title'] = li.xpath('./span[@class="state3"]/a/text()').get()
            item['href'] = BASE_URL + li.xpath('./span[@class="state3"]/a/@href').get()
            item['response_time'] = re.findall('等待处理：(.*)', li.xpath('./span[@class="state4"]/text()').get().strip())[0]
            item['publish_time'] = response.xpath('/html/body/div[2]/div[3]/ul[2]/li[1]/span[5]/text()').get()
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item': item}
            )
        # 翻页
        next_url = BASE_URL + response.xpath('//div[@class="mr-three paging-box"]/a[2]/@href').get()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    # 处理详情页
    def parse_detail(self, response):
        item = response.meta['item']
        item['content_text'] = response.xpath('//div[@class="details-box"]/pre/text()').get()
        item['content_img'] = response.xpath('//div[@class="clear details-img-list Picture-img"]/img/@src').getall()
        yield item
