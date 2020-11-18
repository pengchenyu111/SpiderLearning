from urllib.parse import urljoin


# 第一个参数是base_url,只能设置scheme、netloc和path
# 第二个参数若不是完整的url，则会附到第一个参数上去，并按需要添加 /
# 第二个参数若是完整url，则直接返回第二个参数的值

# 输出https://www.jd.com/index.html
print(urljoin('https://www.jd.com', 'index.html'))
# 输出https://www.taobao.com
print(urljoin('https://www.jd.com', 'https://www.taobao.com'))
# 输出https://www.taobao.com/index.html
print(urljoin('https://www.jd.com/index.html', 'https://www.taobao.com/index.html'))
# 输出https://www.jd.com/index.php?name=Bill&age=30
print(urljoin('https://www.jd.com/index.php', '?name=Bill&age=30'))
# 输出https://www.jd.com/index.php?name=Bill
print(urljoin('https://www.jd.com/index.php?value=123', '?name=Bill'))
