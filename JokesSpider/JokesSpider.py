import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

jokeLists = []


def verifySex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'


def getJoke(url):
    res = requests.get(url)
    # 获取用户名字
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    # 获取用户等级，\D表示[^0-9]
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    # 获取用户性别
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    # 获取文章内容
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    # 获取笑脸数
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', res.text, re.S)
    # 获取评论数
    comments = re.findall('<i class="number">(\d+)</i> 评论', res.text, re.S)

    # zip函数：将上诉获得的数据的对应索引的元素放在一起
    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {
            'id': id,
            'level': level,
            'sex': verifySex(sex),
            'content': content,
            'laugh': laugh,
            'comment': comment
        }
        jokeLists.append(info)


# 这种写法就离谱？还可以这么写
urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 31)]
for url in urls:
    getJoke(url)
for joke in jokeLists:
    f = open('./jokes.txt', 'a+')
    try:
        f.write(joke['id'] + '\n')
        f.write(joke['level'] + '\n')
        f.write(joke['sex'] + '\n')
        f.write(joke['content'] + '\n')
        f.write(joke['laugh'] + '\n')
        f.write(joke['comment'] + '\n\n')
        f.close()
    except UnicodeEncodeError:
        pass
