from urllib3 import *
# urlencode函数在urllib.parse模块中
from urllib.parse import urlencode

# 调用disable_warnings函数可以阻止显示警告消息
disable_warnings()
# 创建PoolManager类的实例
http = PoolManager()
'''
# 下面的代码通过组合URL的方式向百度发送请求
url = 'http://www.baidu.com/s?' + urlencode({'wd':'极客起源'})
print(url)
response = http.request('GET', url)
'''
url = 'http://www.baidu.com/s'
# 直接使用fields关键字参数指定GET请求字段
response = http.request('GET', url, fields={'wd': '极客起源'})
# 获取百度服务端的返回值（字节形式），并使用UTF-8格式对其进行解码
data = response.data.decode('UTF-8')
# 输出百度服务端返回的内容
print(data)
