from urllib import request, error

try:
    # bad request 400
    response = request.urlopen('http://www.jd123.com/test.html')
except error.URLError as e:
    print(e.reason)
try:
    # not found 404 域名存在而资源不存在
    response = request.urlopen('https://geekori.com/abc.html')
except error.URLError as e:
    print(e.reason)
try:
    # 域名不存在，DNS解析错误
    response = request.urlopen('https://geekori123.com/abc.html')
except error.URLError as e:
    print(e.reason)
try:
    # 超时
    response = request.urlopen('https://baidu.com', timeout=0.000001)
except error.URLError as e:
    print(e.reason)
