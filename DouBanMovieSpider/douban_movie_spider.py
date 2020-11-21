import requests
from lxml import etree
import re
import sqlite3
import os

import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}


def get_movie_url(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    movie_hrefs = selector.xpath('//div[@class="hd"]/a/@href')
    for movie_href in movie_hrefs:
        get_movie_info(movie_href)


def get_movie_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    try:
        name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        director = selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        actors = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]
        actor = actors.xpath('string(.)')
        style = re.findall('<span property="v:genre">(.*?)</span>', html.text, re.S)[0]
        country = re.findall('<span class="pl">制片国家/地区:</span> (.*?)<br/>', html.text, re.S)[0]
        release_time = re.findall('上映日期:</span>.*?>(.*?)</span>', html.text, re.S)[0]
        time = re.findall('片长:</span>.*?>(.*?)</span>', html.text, re.S)[0]
        score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
        global id

        id += 1
        movie = (
        id, str(name), str(director), str(actor), str(style), str(country), str(release_time), str(time), score)
        print(movie)
        cursor.execute(
            "insert into movies (id,name,director,actor,style,country,release_time,time,score) values(?,?,?,?,?,?,?,?,?)",
            movie)
        conn.commit()

    except IndexError:
        pass


if __name__ == '__main__':
    id = 0
    dbPath = 'movie.sqlite'
    if os.path.exists(dbPath):
        os.remove(dbPath)
    # 创建SQLite数据库
    conn = sqlite3.connect(dbPath)
    # 获取sqlite3.Cursor对象
    cursor = conn.cursor()
    # 创建persons表
    cursor.execute('''CREATE TABLE movies
     (id INT  NOT NULL,
      name           CHAR(50)    NOT NULL,
      director       CHAR(50)     NOT NULL,
      actor         CHAR(50)  NOT NULL,
      style         CHAR(50) NOT NULL,
      country        CHAR(50) NOT NULL,
      release_time   CHAR(50) NOT NULL,
      time CHAR(50) NOT NULL,
      score REAL NOT NULL          
      );''')

    # 修改数据库后必须调用commit方法提交才能生效
    conn.commit()

    print('创建数据库成功')

    urls = ['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        get_movie_url(url)
        time.sleep(1)
    conn.close()
