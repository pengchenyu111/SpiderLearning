# SpiderLearning

学习Python爬虫的一些资料、记录与心得

# 使用许可

该仓库只用于自己的学习记录，**如涉及侵犯个人或团体利益，请与我联系，我将主动撤销一切相关数据，谢谢**！

该仓库中所爬取的一些数据集仅限用于学习研究目的，我不能保证数据的正确性以及任何场景的适用性。对于使用这份数据的其他用户，必须严格遵循下列条件:

1. 未经许可，用户不得将此数据集用于任何商业或收入交易用途。
2. 未经单独许可，用户不得重新转发数据。
3. 用户在使用数据集时，必须声明数据来源。

在任何情况下，我们均不对因使用这些数据而造成的任何损失承担责任（包括但不限于数据丢失或数据不准确）。如果您有任何其他问题或意见，请发送电子邮件至: iampengchenyu@163.com



# 项目

- BlogSpider：抓取博客园首页的文章列表的url和title

- CinemaSpider：抓取猫眼电影Top100
- JokesSpider：抓取糗事百科文本段子
- NovelSpider：抓取斗破小说网的文章
- DouBanBookSpider：爬取豆瓣TOP250书籍的基本信息
- QiDianNovelSpider：爬取起点中文网全部作品的基本信息
- XiaoZhuRentSpider：抓取小猪民宿的房源基本信息
- KouGouRankSpider：抓取酷狗网络红歌排行榜基本信息



# 知识点

## RegularExpression

正则表达式讲解，help.md含详解

## urllib

urllib的学习记录

- urllib.request：基本HTTP请求模块
- urllib.error：异常处理模块
- urllib.parse：工具模块，拆分、解析、合并URL的API
- urllib.robotparser：识别网站的robots.txt文件，判断哪些网站可以抓取

## urllib3

相较于urllib，有以下优点：

- 线程安全
- 连接池
- 使用multipart编码上传文件
- 客户端SSL/TLS验证
- 支持HTTP和SOCKS代理

## requests

相比urllib和urllib3要简单一些

- 文件上传
- 处理Cookie
- 维持会话Session
- SSL证书验证

## twisted

异步编程模型，Reactor模式

简单demo，Scrapy框架基础。

## lxml、xpath

help.md中含xpath的一些语法知识

## BeautifulSoup

选择结点、方法选择器、CSS选择器