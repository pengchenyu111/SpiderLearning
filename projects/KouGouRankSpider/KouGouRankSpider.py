from lxml import etree
import requests
import xlwt

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie': 'kg_mid=d27aa20f94a54d06fd6416f8166ddf09; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1605868665; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; kg_dfid=3eXgt22MgiMZ17bqLd2t1Ag7; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=d27aa20f94a54d06fd6416f8166ddf09; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1605868686'
}


# 根据一个url获取这个页面
def getOnePage(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except Exception:
        return None


def getRanks(html):
    selector = etree.HTML(html)
    songList = selector.xpath('//div[@id="rankWrap"]/div[2]/ul/li')
    for songInfo in songList:
        singerAndSongName = songInfo.xpath('@title')[0]
        rankInfo = songInfo.xpath('span[3]/text()')[0].strip()
        if rankInfo == '':
            # 前三名格式给其他不一样，多了个strong标签
            rankInfo = songInfo.xpath('span[3]/strong/text()')[0].strip()
        yield {
            'rank': rankInfo,
            'singer': singerAndSongName.split('-')[0].strip(),
            'songName': singerAndSongName.split('-')[1].strip(),
            'time': songInfo.xpath('span/span[@class="pc_temp_time"]/text()')[0].strip()
        }


header = ['排名', '歌手', '歌曲名', '时长']
songsBook = xlwt.Workbook(encoding='utf-8')
sheet = songsBook.add_sheet('酷狗网络红歌榜')
for h in range(len(header)):
    sheet.write(0, h, header[h])

urls = [
    'https://www.kugou.com/yy/rank/home/{}-23784.html?from=rank'.format(str(i))
    for i in range(1, 10)
]
i = 1

for url in urls:
    page = getOnePage(url)
    for song in getRanks(page):
        print(str(url) + "*" + str(song))
        sheet.write(i, 0, song['rank'])
        sheet.write(i, 1, song['singer'])
        sheet.write(i, 2, song['songName'])
        sheet.write(i, 3, song['time'])
        i += 1
songsBook.save('酷狗红歌榜.xls')
