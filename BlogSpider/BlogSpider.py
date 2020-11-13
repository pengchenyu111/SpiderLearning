from urllib3 import *
from re import *

# 获取一个连接池的实例
http = PoolManager()
# 禁止显示警告信息
disable_warnings()


# 下载url对应的页面
def download(url):
    result = http.request('GET', url)
    # 获取HTML代码
    htmlStr = result.data.decode('utf-8')
    return htmlStr


# 分析HTML代码
def analyse(htmlStr):
    # 获取所有class属性为post-item-title的a标签
    aList = findall('<a[^>]*post-item-title[^>]*>[^<]*</a>', htmlStr)
    result = []
    # 提取节点中的URL和标题
    for a in aList:
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]', a)
        if g != None:
            url = g.group(1)
        index1 = a.find(">")
        index2 = a.rfind("<")
        title = a[index1 + 1:index2]
        d = {}
        d['url'] = url
        d['title'] = title
        result.append(d)
    return result


def crawler(url):
    html = download(url)
    blogList = analyse(html)
    for blog in blogList:
        print("title:", blog["title"])
        print("url:", blog["url"])


# 抓取入口
crawler('https://www.cnblogs.com')
