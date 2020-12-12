from lxml import *
from lxml import etree
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie': 'll="118172"; bid=an8WAFbEqG8; _vwo_uuid_v2=DB9B53B65CD89C7EB6AC478833F29C8DE|41e8f854f575e94badfb7ab8647a4bb4; douban-fav-remind=1; __gads=ID=dcefcc35efb93c30-228083cbaec40095:T=1605108669:RT=1605108669:S=ALNI_MZOCmDPHgfDeS4v4-4I4VUo2Iy7KA; gr_user_id=4a01320a-b37c-4790-8812-e47811abdd52; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=c9211a5c-d805-4621-91ab-2f5d4329647b; gr_cs1_c9211a5c-d805-4621-91ab-2f5d4329647b=user_id%3A0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1605788353%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D_8BjE1lhNZ56FEYtVt7ITyk83Np2tLze8KRYIoyEJ7L-8I_hs1deG1GnHBNSFjcW%26wd%3D%26eqid%3Daa1571e90002df6f000000055fb662bd%22%5D; _pk_ses.100001.3ac3=*; ap_v=0,6.0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_c9211a5c-d805-4621-91ab-2f5d4329647b=true; __utma=30149280.76123585.1601126807.1605235293.1605788353.9; __utmc=30149280; __utmz=30149280.1605788353.9.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=81379588.186266916.1605788354.1605788354.1605788354.1; __utmc=81379588; __utmz=81379588.1605788354.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=HrewzqgX6nFIti33jHVG05OJtnrpvWeE; __utmb=30149280.4.10.1605788353; __utmb=81379588.4.10.1605788354; _pk_id.100001.3ac3=409f23ff58725abb.1605788353.1.1605788400.1605788353.'
}


def getOnePage(url):
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None


def parseOnePage(html):
    selector = etree.HTML(html)
    items = selector.xpath('//tr[@class="item"]')
    for item in items:
        book_infos = item.xpath('td/p/text()')[0]
        yield {
            'name': item.xpath('td/div/a/@title')[0],
            'url': item.xpath('td/div/a/@href')[0],
            'img': item.xpath('td/a/img/@src')[0],
            'author': book_infos.split('/')[0],
            'publisher': book_infos.split('/')[-3],
            'date': book_infos.split('/')[-2],
            'price': book_infos.split('/')[-1]
        }


def save(content):
    with open('top250books.txt', 'at', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def getTop250(url):
    html = getOnePage(url)
    for item in parseOnePage(html):
        print(item)
        save(item)


# url的规则是：每页显示25条
urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]

# 开始爬取
for url in urls:
    getTop250(url)
