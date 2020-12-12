from lxml import etree
import requests
import xlwt

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie': 'abtest_ABTest4SearchDate=b; distinctId=175e11111b1a17-0aeb2aadddd60d-930346c-2359296-175e11111b296f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22175e11111b1a17-0aeb2aadddd60d-930346c-2359296-175e11111b296f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22175e11111a2abd-07469016b0905-930346c-2359296-175e11111a34da%22%7D; Hm_lvt_92e8bc890f374994dd570aa15afc99e1=1605798794; _uab_collina=160579882384326461649766; xz_guid_4se=98cbaee0-2251-4a2d-a2fa-61e1574e4a38; wttXMuWwbC=9e981fca9fefb9a7d93126e3d75cba57cfe78eda; ATNgmRNkrw=1605810475; xzuuid=0286f8c2; rule_math=xxhzu1wmwzj; Hm_lpvt_92e8bc890f374994dd570aa15afc99e1=1605810497'}


# 得到一个页面
def getOnePage(url):
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None


# 解析一个页面
def parseOnePage(html):
    selector = etree.HTML(html)
    detailUrls = selector.xpath('//a[@class="resule_img_a"]/@href')
    return detailUrls


# 获取一个房源中的详细信息
def getOneRentDetail(detailUrl):
    html = getOnePage(detailUrl)
    selector = etree.HTML(str(html))
    houseInfo = {'title': selector.xpath('//h4/em/text()')[0],
                 'address': selector.xpath('//div[@class="pho_info"]/p/@title')[0],
                 'price': selector.xpath('//div[@class="day_l"]/span/text()')[0],
                 'poster': selector.xpath('//img[@id="curBigImage"]/@src')[0],
                 'shortDescription': checkNone(selector, '//div[@id="introducePart"]/div[1]/div[2]/div[1]/p/text()'),
                 'innerDetail': checkNone(selector, '//div[@id="introducePart"]/div[2]/div[2]/div/p/text()'),
                 'href': detailUrl,
                 'hostImg': selector.xpath('//div[@class="member_pic"]/a/img/@src')[0],
                 'hostName': selector.xpath('//a[@class="lorder_name"]/@title')[0],
                 'hostSex': getHostSex(selector.xpath('//a[@class="lorder_name"]/following-sibling::span/@class')[0])
                 }
    return houseInfo


def checkNone(selector, xpath):
    if len(selector.xpath(xpath)) != 0:
        return selector.xpath(xpath)
    else:
        return '暂无'


# 根据class属性获取性别
def getHostSex(str):
    if str == 'member_boy_ico':
        return '男'
    elif str == 'member_girl_ico':
        return '女'
    else:
        return '未知'


# print(getOnePage('https://hf.xiaozhu.com/fangzi/144895497897.html'))

header = ['标题', '地址', '价格', '封面', '简介', '内部情况', '链接', '主人图片', '主人名字', '主人性别']
house = xlwt.Workbook(encoding='utf-8')
sheet = house.add_sheet('房源信息')
for h in range(len(header)):
    sheet.write(0, h, header[h])

urls = [
    'https://hf.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i))
    for i in range(2, 3)]
i = 1
for url in urls:
    detailUrls = parseOnePage(getOnePage(url))
    for detailUrl in detailUrls:
        rentInfo = getOneRentDetail(detailUrl)
        print(rentInfo)
        sheet.write(i, 0, rentInfo['title'])
        sheet.write(i, 1, rentInfo['address'])
        sheet.write(i, 2, rentInfo['price'])
        sheet.write(i, 3, rentInfo['poster'])
        sheet.write(i, 4, rentInfo['shortDescription'])
        sheet.write(i, 5, rentInfo['innerDetail'])
        sheet.write(i, 6, rentInfo['href'])
        sheet.write(i, 7, rentInfo['hostImg'])
        sheet.write(i, 8, rentInfo['hostName'])
        sheet.write(i, 9, rentInfo['hostSex'])
        i += 1

house.save('house.xls')
