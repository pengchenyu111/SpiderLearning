import requests

# 不使用Session
requests.get('http://httpbin.org/cookies/set/name/Bill')
# 第二次发送请求，这两次请求不在一个Session中，故第一次发送的Cookies在第二次请求中是无法获得的
r1 = requests.get('http://httpbin.org/cookies')
print(r1.text)

# 使用Session
session = requests.Session()
session.get('http://httpbin.org/cookies/set/name/Bill')
r2 = session.get('http://httpbin.org/cookies')
print(r2.text)
