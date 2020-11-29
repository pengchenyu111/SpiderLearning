# 什么是Scrapy

Scrapy 是用 Python 实现的一个为了爬取网站数据、提取结构性数据而编写的应用框架。

Scrapy 常应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。通常我们可以很简单的通过 Scrapy 框架实现一个爬虫，抓取指定网站的内容或图片。

# 框架

**整体在Scrapy Engine的调度下，首先运行的是Scheduler，Scheduler从下载队列中去一个URL，将这个URL交给Downloader，Downloader下载这个URL对应的Web资源，然后将下载好的原始数据给Spiders，Spiders会从原始数据中提取有用的信息，最后将提出的数据交给Item Pipeline，Item Pipeline可以将数据保存到数据库文本文件或其他存储介质上。**

![image-20201127160936991](C:\Users\PENGZI\AppData\Roaming\Typora\typora-user-images\image-20201127160936991.png)

- **Scrapy Engine(引擎)**: 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。
- **Scheduler(调度器)**: 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。
- **Downloader（下载器）**：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理，
- **Spider（爬虫）**：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器).
- **Item Pipeline(管道)**：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方。
- **Downloader Middlewares（下载中间件）**：你可以当作是一个可以自定义扩展下载功能的组件。
- **Spider Middlewares（Spider中间件）**：你可以理解为是一个可以自定扩展和操作引擎和Spider中间通信的功能组件（比如进入Spider的Responses;和从Spider出去的Requests）

# 使用

创建项目

```python
scrapy startproject [项目名]
```

创建爬虫

```python
# 需要先进入项目：cd ...
scrapy genspider [爬虫名] [允许爬取的范围]
```

启动爬虫

```python
scrapy crawl [爬虫名]
```

创建crawlspider

```python
scrapy genspider -t crawl [爬虫名] [允许爬取的范围]
```

------



# CrawlSpider

**LinkExtractor 更多常见参数：** 

- allow：满足括号中．‘正则表达式”的 URL 会被提取，如果为空．则全部匹配 
- deny ：满足括号中“正则表达式”的 URL 一定不提取（优先级高于 allow ）。 
- allow_domains ：会被提取的链接的 domains
- deny_domains ：一定不会被提取链接的 domains 
- restrlct_xpaths ：使用 xpath 表达式．和 allow 共同作用过滤链接．xpath 满足范圈内的 url地址会被提取 

**spiders . Rule 常见参数：** 

- link_extractor 是一个LinkExtractor 对象，用于定义要提取的链接 
- callback ：从 link_extractor 中每获取到链接时，参数所指定的值作为回调函数 
- follow：是一个布尔值，指定了根据该规则从 response 提取的链接是否要跟进．如果 callback 为 None , follow 默认为朴True ．否则默认为 False 
-  process_links：指定该 spider中哪个的函数将会被调用，从 Iink _ extractor 中获取到链接列表时将会调用该函数，该方法主贾用来过滤url
- process_request ：指定该 spider 中哪个的函数将会被调用，该规则提取到每个 request 时都会调用该函数，用来过滤request



------



# 细节

1. 在进行列表页加多层详情页时，可能出现有的爬取内容是重复的，这是因为**深拷贝与浅拷贝**的原因，这在编码时要看item是共用的还是每个内容一个item。
   处理：使用**deepcopy**
   详情见：https://www.bilibili.com/video/BV1Jx411d7F2?p=13 25:34

