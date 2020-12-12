import threading
import datetime
import requests
from bs4 import BeautifulSoup
import re
import time
import csv

starttime = datetime.datetime.now()

lock = threading.Lock()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie': 'll="118172"; bid=an8WAFbEqG8; _vwo_uuid_v2=DB9B53B65CD89C7EB6AC478833F29C8DE|41e8f854f575e94badfb7ab8647a4bb4; douban-fav-remind=1; gr_user_id=4a01320a-b37c-4790-8812-e47811abdd52; __utmz=30149280.1605788353.9.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=fA2qOWrfgXqByQZS6TvY2u9Upcy9ieaU; Hm_lvt_cfafef0aa0076ffb1a7838fd772f844d=1605949942; __gads=ID=dcefcc35efb93c30-2272a880d9c4008b:T=1605950007:RT=1605950007:S=ALNI_Maqda8alXBrEKTnzCzXPtvLTMNSTw; viewed="1403307_3040149_2995812_6082808_6789551"; push_doumail_num=0; __utmv=30149280.16494; push_noty_num=0; ap_v=0,6.0; __utmc=30149280; _pk_ses.100001.afe6=*; __utma=30149280.76123585.1601126807.1606030209.1606036500.15; __utmt=1; dbcl2="164948645:Lqf66FfVk3A"; _pk_id.100001.afe6=bf4b8e2ac9e5e78b.1605949932.5.1606037019.1606030242.; ck=6XOJ; __utmb=30149280.3.10.1606036500'
}

filename = 'music2.csv'


def save_csv(filename, info):
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['name', 'author', 'style', 'time', 'publisher', 'score', 'poster']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(info)


# global：需要在一个函数内修改全局变量
# del：
def get_url():
    global urls
    lock.acquire()
    if len(urls) == 0:
        lock.release()
        return ""
    else:
        url = urls[0]
        # 提取一个url后，将其从列表中删除
        del urls[0]
    lock.release()
    return url


print(time.time())


def get_url_music(url, thread_name):
    html = requests.get(url, headers=headers)

    soup = BeautifulSoup(html.text, 'lxml')

    aTags = soup.find_all("a", attrs={"class": "nbg"})
    for aTag in aTags:
        get_music_info(aTag['href'], thread_name)


def get_music_info(url, thread_name):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    name = soup.find(attrs={'id': 'wrapper'}).h1.span.text
    author = soup.find(attrs={'id': 'info'}).find('a').text
    styles = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(styles) == 0:
        style = '未知'
    else:
        style = styles[0].strip()
    time = re.findall('发行时间:</span>&nbsp;(.*?)<br />', html.text, re.S)[0].strip()
    publishers = re.findall('<span class="pl">出版者:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(publishers) == 0:
        publisher = '未知'
    else:
        publisher = publishers[0].strip()

    score = soup.find(class_='ll rating_num').text
    poster = soup.find(attrs={'id': 'mainpic'}).span.a.img['src']
    info = {
        'name': name,
        'author': author,
        'style': style,
        'time': time,
        'publisher': publisher,
        'score': score,
        'poster': poster
    }
    print(thread_name, info)
    save_csv(filename, info)


class SpiderThread(threading.Thread):  # 继承父类threading.Thread

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            url = get_url()
            if url != "":
                get_url_music(url, self.name)
            else:
                break


if __name__ == '__main__':
    url_index = 0
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0, 200, 25)]
    print(len(urls))

    # 设置文件
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['name', 'author', 'style', 'time', 'publisher', 'score', 'poster']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    # 创建新线程
    thread1 = SpiderThread('thread1')
    thread2 = SpiderThread('thread2')
    thread3 = SpiderThread('thread3')
    thread4 = SpiderThread('thread4')

    # 开启线程
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    print("退出爬虫")

    endtime = datetime.datetime.now()
    print('需要时间：', (endtime - starttime).seconds, '秒')
