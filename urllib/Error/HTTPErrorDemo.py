from urllib import request, error
import socket

# HTTPError是URLError的子类
# time out 无法用HTTPError捕捉
# 注意并不是reason属性每次返回的都是字符串类型，如timeout返回的是socket.timeout的实例

try:
    response = request.urlopen('http://www.jd123.com/test.html')
except error.HTTPError as e:
    print(type(e.reason))
    print('三个属性：' + e.reason, e.code, e.headers)
try:
    response = request.urlopen('https://baidu.com', timeout=0.00001)
except error.HTTPError as e:
    print('error.HTTPError：', e.reason)
except error.URLError as e:
    print(type(e.reason))
    print('error.URLError：', e.reason)
    if isinstance(e.reason, socket.timeout):
        print('超时错误')
else:
    print('成功发送请求')
