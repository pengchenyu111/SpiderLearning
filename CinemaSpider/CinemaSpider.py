import json
from urllib3 import *

import re
import time

disable_warnings()
http = PoolManager()


def getOnePage(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Cookie': '__mta=45528731.1603529896584.1605349172806.1605349181775.27; _lxsdk_cuid=17559b02139c8-05da2b37b85a26-f7b1332-240000-17559b02139c8; uuid_n_v=v1; uuid=0DCE06D015D711EBBFF0EDDBFC80D580EF0C9ECCC3054F109813EE8C626025AA; _lxsdk=0DCE06D015D711EBBFF0EDDBFC80D580EF0C9ECCC3054F109813EE8C626025AA; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=cb845ee07e7e548818d49ef857f2b993c37ee0db579303d3e2937699c88657cd; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1603529896,1605342364; __mta=45528731.1603529896584.1605349172806.1605349179256.27; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1605349182; _lxsdk_s=175c611f490-c0f-f7-c4%7C%7C46'
        }
        response = http.request('GET', url, headers=headers)

        data = response.data.decode('utf-8')

        if response.status == 200:
            return data
        return None
    except Exception:
        return None


# 这是一个生成器函数，可以对返回值迭代
def parseOnePage(html):
    # re.S：.的作用扩展到整个字符串，包括\n，默认.只针对一行
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?href="(.*?)".*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'id': item[1].strip()[7:],
            'url': 'https://maoyan.com' + item[1],
            'image': item[2],
            'title': item[3],
            'actor': item[4].strip()[3:],
            'time': item[5].strip()[5:],
            'score': item[6] + item[7]
        }


def save(content):
    with open('board.txt', 'a', encoding='utf-8') as f:
        # 将对象转为json字符串，ensure_ascii=False表示返回的值可以包含非ASCLL字符
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def getBoard(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = getOnePage(url)

    for item in parseOnePage(html):
        print(item)
        save(item)


for i in range(10):
    getBoard(offset=i * 10)
    time.sleep(1)
