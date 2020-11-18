import urllib.request

response = urllib.request.urlopen('https://www.jd.com')

# urlopen函数返回的书籍类型为：http.client.HTTPResponse
print('response的类型：', type(response))

# status: 200  msg: OK  version: 11
print('status:', response.status, ' msg:', response.msg, ' version:', response.version)
print('headers:', response.getheaders())
print('headers.Content-Type', response.getheader('Content-Type'))
print(response.read().decode('utf-8'))
