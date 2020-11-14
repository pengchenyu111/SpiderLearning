from urllib import request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}


# 获取小说目录列表，返回每章节
def getCatelogs(url):
    req = request.Request(url=url, headers=headers, method="GET")
    response = request.urlopen(req)
    result = []
    if response.status == 200:
        html = response.read().decode('utf-8')
        # 找到目录列表
        aList = re.findall('<li>.*</li>', html)
        for a in aList:
            # 寻找其中的url和title
            g = re.search('href="([^>"]*)"[\s]*title="([^>"]*)"', a)

            if g != None:
                url = 'http://www.doupoxs.com' + g.group(1)
                title = g.group(2)

                chapter = {'title': title, 'url': url}
                result.append(chapter)
    return result


# 获取每章节内容
def getChapterContent(chapters):
    for chapter in chapters:
        req = request.Request(url=chapter['url'], headers=headers, method="GET")
        response = request.urlopen(req)
        if response.status == 200:
            # 写入本地文件
            f = open('novel-nananwudi/' + chapter['title'] + '.txt', 'a+')
            contents = re.findall('<p>(.*?)</p>', response.read().decode('utf-8'))
            for content in contents:
                f.write(content + '\n')
            f.close()
            print(chapter['title'], chapter['url'])


getChapterContent(getCatelogs('http://www.doupoxs.com/nalanwudi/'))
