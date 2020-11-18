from urllib3 import *

disable_warnings()
http = PoolManager()
url = 'https://www.baidu.com'
response = http.request('GET', url)
# 输出HTTP响应头信息（以字典形式返回HTTP响应头信息）
for key in response.info().keys():
    print(key, ':', response.info()[key])
