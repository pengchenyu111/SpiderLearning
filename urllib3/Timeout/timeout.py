from urllib3 import *

disable_warnings()
# 通过PoolManager类的构造方法指定默认的连接超时和读超时
http = PoolManager(timeout=Timeout(connect=2.0, read=2.0))
url1 = 'https://www.baidu1122.com'
url2 = 'http://httpbin.org/delay/3'
try:
    # 此处代码需要放在try…except中，否则一旦抛出异常，后面的代码将无法执行
    # 下面的代码会抛出异常，因为域名www.baidu1122.com并不存在
    # 由于连接超时设为2秒，
    http.request('GET', url1, timeout=Timeout(connect=2.0, read=4.0))
except Exception as e:
    print(e)
print('------------')
# 由于读超时为4秒，而url2指定的Url在3秒后就返回数据，所以不会抛出异常，
# 会正常输出服务器的返回结果
response = http.request('GET', url2, timeout=Timeout(connect=2.0, read=4.0))
print(response.info())
print('------------')
print(response.info()['Content-Length'])
# 由于读超时为2秒，所以会在2秒后抛出读超时异常
http.request('GET', url2, timeout=Timeout(connect=2.0, read=2.0))
