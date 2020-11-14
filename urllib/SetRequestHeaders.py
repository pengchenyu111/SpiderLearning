from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Host': 'httpbin.org',
    # who为自定义字段
    'who': 'Python Scrapy'
}

# 定义表单数据
dict = {
    'name': 'Bill',
    'age': 30
}
# 将表单数据转换为bytes形式
data = bytes(parse.urlencode(dict), encoding='utf-8')
# 使用Request类构造
req = request.Request(url=url, data=data, headers=headers, method="POST")

response = request.urlopen(req)
print(response.read().decode('utf-8'))
