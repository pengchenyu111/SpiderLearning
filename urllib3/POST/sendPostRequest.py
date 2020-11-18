from urllib3 import *

disable_warnings()
http = PoolManager()
# 指定要提交HTTP POST请求的URL，/register是路由
url = 'http://localhost:5000/register'
# 向服务端发送HTTP POST请求，用fields关键字参数指定HTTP POST请求字段名和值
response = http.request('POST', url, fields={'name': '李宁', 'age': 18})
# 获取服务端返回的数据
data = response.data.decode('UTF-8')
# 输出服务端返回的数据
print(data)
