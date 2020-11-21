import requests
from bs4 import BeautifulSoup
import re
import csv
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}


def get_url_music(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')

    # 获取每个歌曲链接的a标签
    aTags = soup.find_all("a", attrs={"class": "nbg"})
    for aTag in aTags:
        get_music_info(aTag['href'])


def save_csv(filename, info):
    with open(filename, 'a', encoding='utf-8') as f:
        fieldnames = ['name', 'author', 'style', 'time', 'publisher', 'score', 'poster']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(info)


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
    save_csv(filename, info)


if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
    filename = 'music.csv'
    with open(filename, 'w', encoding='utf-8') as f:
        fieldnames = ['name', 'author', 'style', 'time', 'publisher', 'score', 'poster']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    for url in urls:
        get_url_music(url)
        time.sleep(1)
