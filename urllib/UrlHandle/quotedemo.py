from urllib.parse import quote, unquote

# 与urlencode函数不同的是，urlencode函数需要传进一个字典，包含key和value，而quote只需要传入一个字符串即可
keyword = '李宁'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
url = unquote(url)
print(url)
