import xlwt
import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cokkie': '_yep_uuid=6574059d-78db-d8e7-7d39-a0a7b4de8bba; _csrfToken=Bd4ZrcqOQQnq0VDkaDOQHa1EDUFqP9bxLeL70ewf; newstatisticUUID=1605790560_2078709458; e1=%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22qd_C44%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22qd_H_yeyou%22%2C%22l1%22%3A3%7D'
}


def getOnePage(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')
    for info in infos:
        style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]

        yield {
            'title': info.xpath('div[2]/h4/a/text()')[0],
            'author': info.xpath('div[2]/p[1]/a[1]/text()')[0],
            'style': style_1 + '·' + style_2,
            'complete': info.xpath('div[2]/p[1]/span/text()')[0],
            'introduce': info.xpath('div[2]/p[2]/text()')[0].strip(),
            'img': 'http:' + info.xpath('div[@class="book-img-box"]/a/img/@src')[0]
        }


def writeIntoExcel(novels, file):
    # 生成Excel文件
    header = ['标题', '作者', '类型', '完成度', '介绍', '图片地址']
    sheet = file.add_sheet('novels')
    for h in range(len(header)):
        sheet.write(0, h, header[h])
    # 写入小说信息
    i = 1
    for novel in novels:
        print(novel)
        time.sleep(0.1)
        sheet.write(i, 0, novel['title'])
        sheet.write(i, 1, novel['author'])
        sheet.write(i, 2, novel['style'])
        sheet.write(i, 3, novel['complete'])
        sheet.write(i, 4, novel['introduce'])
        sheet.write(i, 5, novel['img'])
        i += 1


header = ['标题', '作者', '类型', '完成度', '介绍', '图片地址']
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('novels')
for h in range(len(header)):
    sheet.write(0, h, header[h])

urls = [
    'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page={}'.format(str(i))
    for i in range(1, 10)]
i = 1
for url in urls:
    novels = getOnePage(url)
    for novel in novels:
        print(novel)
        time.sleep(0.1)
        sheet.write(i, 0, novel['title'])
        sheet.write(i, 1, novel['author'])
        sheet.write(i, 2, novel['style'])
        sheet.write(i, 3, novel['complete'])
        sheet.write(i, 4, novel['introduce'])
        sheet.write(i, 5, novel['img'])
        i += 1

book.save('novels.xls')
