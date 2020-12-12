import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool

import datetime

starttime = datetime.datetime.now()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie': 'll="118172"; bid=an8WAFbEqG8; _vwo_uuid_v2=DB9B53B65CD89C7EB6AC478833F29C8DE|41e8f854f575e94badfb7ab8647a4bb4; douban-fav-remind=1; gr_user_id=4a01320a-b37c-4790-8812-e47811abdd52; __utmz=30149280.1605788353.9.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=fA2qOWrfgXqByQZS6TvY2u9Upcy9ieaU; Hm_lvt_cfafef0aa0076ffb1a7838fd772f844d=1605949942; __gads=ID=dcefcc35efb93c30-2272a880d9c4008b:T=1605950007:RT=1605950007:S=ALNI_Maqda8alXBrEKTnzCzXPtvLTMNSTw; viewed="1403307_3040149_2995812_6082808_6789551"; push_doumail_num=0; __utmv=30149280.16494; push_noty_num=0; ap_v=0,6.0; __utmc=30149280; _pk_ses.100001.afe6=*; __utma=30149280.76123585.1601126807.1606030209.1606036500.15; __utmt=1; dbcl2="164948645:Lqf66FfVk3A"; _pk_id.100001.afe6=bf4b8e2ac9e5e78b.1605949932.5.1606037019.1606030242.; ck=6XOJ; __utmb=30149280.3.10.1606036500'
}


def get_url_music(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    aTags = soup.find_all("a", attrs={"class": "nbg"})
    for aTag in aTags:
        get_music_info(aTag['href'])


def get_music_info(url):
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
    print(info)


if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0, 100, 25)]
    print(len(urls))
    pool = Pool(processes=4)
    pool.map(get_url_music, urls)
