import scrapy
import re


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/975472588/profile']

    def start_requests(self):
        # 这里不加cookie无法进入个人主页
        cookies = 'anonymid=ki4mbqba-7e5t5a; depovince=GW; _r01_=1; JSESSIONID=abcNezdplcGyXds9TCzyx; ick_login=c95f93ca-3225-4c24-8043-a90444dea1de; taihe_bi_sdk_uid=f3e78c457fc7b40847132e6a2f5102e0; taihe_bi_sdk_session=a97853cfc7a15f1bf9b41341c4e3229a; ick=4ad74aa2-fd8c-4de2-b4a6-28c7bf55bce4; first_login_flag=1; ln_uact=18256510879; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20201130/2200/h_main_D969_0c1b0003c8d9195a.jpg; jebecookies=5c1ad726-169b-4b26-9738-f6f4f6e1df08|||||; _de=DB4EFB3B932773C602B471F641913507; p=f388106656cafdfa287e4d553fe992388; ap=975472588; t=6ae54db882b5eab7a0222f22b128dc988; societyguester=6ae54db882b5eab7a0222f22b128dc988; id=975472588; xnsid=e681a799; ver=7.0; loginfrom=null; wp_fold=0'
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        item = {}
        item['name'] = response.xpath('//h1[@class="avatar_title no_auth"]/text()').get().strip()
        print(item)
        yield scrapy.Request(
            'http://www.renren.com/975472588/profile?v=info_timeline',
            callback=self.parse_detail
            # 这里就不用再加上cookie代码了，scrapy的settings中的COOKIES_ENABLED选项默认帮我们携带之前的cookie
        )

    def parse_detail(self, response):
        pass
