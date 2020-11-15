from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'bill'
password = '1234'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
# 第一个参数是realm，若设置了则必须与服务器设置WWW-Authenticate时指定的realm相同
p.add_password('localhost', url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
