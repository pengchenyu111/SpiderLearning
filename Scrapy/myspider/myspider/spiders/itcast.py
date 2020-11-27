import scrapy
import logging

# 传入__name__是为了显示该log出自于哪个文件
logger = logging.getLogger(__name__)


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名
    allowed_domains = ['itcast.cn']  # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始请求的url地址

    def parse(self, response):
        # 处理start_url地址对应的响应
        # teacher_list = response.xpath("//div[@class='tea_con']//h3//text()").getall()
        # print(teacher_list)

        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            item['name'] = li.xpath(".//h3/text()").get()
            item['title'] = li.xpath(".//h4/text()").get()
            # print(item)
            logger.warning(item)
            # 这里只能返回Request,BaseItem,dict,None,返回其他报错
            yield item
