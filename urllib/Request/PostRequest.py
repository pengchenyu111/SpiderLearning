import urllib.request

# 要发送HTTP请求，需要使用data命名参数，该参数是bytes类型，需要用bytes类将字符串形式的数据转为bytes类型
data = bytes(urllib.parse.urlencode({'name': 'Bill', 'age': 30}), encoding='utf-8')

response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
