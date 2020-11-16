import http.cookiejar
import urllib.request

# 读取自定义的Cookie
filename = 'cookies.txt'
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://127.0.0.1:5000/readCookie')
print(response.read().decode('utf-8'))
