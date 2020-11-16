import http.cookiejar, urllib.request

# 在获取Cookie的同时将Cookie保存为Mozilla浏览器格式或libwww-perl（LWP）格式
filename1 = 'cookies1.txt'
filename2 = 'cookies2.txt'
cookie1 = http.cookiejar.MozillaCookieJar(filename1)
cookie2 = http.cookiejar.LWPCookieJar(filename2)
handler1 = urllib.request.HTTPCookieProcessor(cookie1)
handler2 = urllib.request.HTTPCookieProcessor(cookie2)
opener1 = urllib.request.build_opener(handler1)
opener2 = urllib.request.build_opener(handler2)
opener1.open('http://www.baidu.com')
opener2.open('http://www.baidu.com')
cookie1.save(ignore_discard=True, ignore_expires=True)
cookie2.save(ignore_discard=True, ignore_expires=True)
